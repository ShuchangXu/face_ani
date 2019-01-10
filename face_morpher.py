import facemorpher

src_imgpaths = facemorpher.list_imgpaths('res/src_frames')
des_imgpath = 'res/des.jpg'
facemorpher.morph_ani(src_imgpaths, des_imgpath, num_pics=47, fps_in=24,
                      out_frames='res/des_frames', out_video='res/output.avi', plot=True)

# srcpath = next(srcpaths)

# imgpaths = facemorpher.list_imgpaths(src_image=srcpath, dest_image='res/des.png')
# facemorpher.morpher(imgpaths, num_frames=47, out_frames='res/des', background='white')
# # for srcpath in srcpaths:
#     imgpaths = facemorpher.list_imgpaths(src_image=srcpath, dest_image='res/des.png')
#     facemorpher.morpher(imgpaths)