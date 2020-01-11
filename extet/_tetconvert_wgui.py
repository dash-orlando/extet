'''
TETGEN converter to Houdini

FUNCTION:
    This programs converts TetGen output files (.node, .ele, .face, .edges) into a .off mesh

Note:
    - Made in Python 2.7 to support direct compatibility with Houdini

'''

## Libraries
import tkFileDialog


## Browse for input .OFF file
#
#   TO DO:
#   - Need to add warning message for no .OFF files
#
input_filepath          = tkFileDialog.askopenfilename().encode('utf-8')
input_filename          = input_filepath.split('/')[-1]
input_filename_wo_ext   = input_filename.split('.')[0]
input_extension         = input_filename.split('.')[-1]
input_path              = input_filepath[0:(len(input_filepath)-len(input_filename))]

# print input_filename, input_filename_wo_ext, input_extension

#filename                = 'geo_mesh.1'
#output                  = 'geo_mesh.1.conv.off'

tetgen_ext = ['edge','ele','face','node']
tetgen_filename = []
for i in range(0, len(tetgen_ext)):
    tetgen_filename.append( '{}{}.1.{}'.format( input_path,
                                                input_filename_wo_ext,
                                                tetgen_ext[i] ) )


output_filename         = '{}{}.conv.off'.format( input_path,
                                                  input_filename_wo_ext )

#print input_filename, output_filename, tetgen_filename


## read on the basis of need
## first, we always read node...

cnt = 0
node_index = []
node_x = []
node_y = []
node_z = []
with open( tetgen_filename[3] ) as fnode:
    for line in fnode:
        line = (' '.join((line.strip('\n')).split())).split(' ') # this eliminates \n, the extra ' ', and finally considers single ' ' as delimiters
        #print line

        if cnt == 0:
            pass
        elif cnt > 0 and line[0] != '#':
            node_index.append( line[0] )
            node_x.append( line[1] )
            node_y.append( line[2] )
            node_z.append( line[3] )

        cnt =+ 1

# second, we read the face file...

cnt = 0
face_index = []
node_a = []
node_b = []
node_c = []
with open( tetgen_filename[2] ) as fface:
    for line in fface:
        line = (' '.join((line.strip('\n')).split())).split(' ') # this eliminates \n, the extra ' ', and finally considers single ' ' as delimiters
        #print line

        if cnt == 0:
            pass
        elif cnt > 0 and line[0] != '#':
            face_index.append( line[0] )
            node_a.append( line[1] )
            node_b.append( line[2] )
            node_c.append( line[3] )

        cnt =+ 1

# finally, we write the .off file
with open( output_filename, 'w+' ) as fout:
    #for i in range(0, (len(node_index) + len(face_index) + 2)):
    fout.write( "OFF\n" )
    fout.write( "{} {} 0\n".format( len(node_index), len(face_index) ) )
    for i in range( 0, len(node_index) ):
        fout.write( "{} {} {}\n".format( node_x[i], node_y[i], node_z[i] ) )
    for i in range( 0, len(face_index) ):
        fout.write( "3 {} {} {}\n".format( node_a[i], node_b[i], node_c[i] ) )

    fout.close()       

