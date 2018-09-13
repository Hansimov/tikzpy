import os
from math import *
from datetime import date, datetime, timedelta
import threading

preamble = []
all_tikz_cmds = []

preamble = [
    '\\documentclass[tikz, border=0pt]{standalone}\n',
    '\\usepackage{tikz}',
    '\\usetikzlibrary{calc}',
    '\\usepackage[skins]{tcolorbox}',
    '\\usepackage{graphicx}',
    '\\usepackage{xcolor}',
    # '\\usepackage{ulem}',
    # '\\usepackage{calc}',
    '\\usepackage{amssymb}',
    '\\usepackage{amsmath}',
    # '\\usepackage{bm}',
    # '\\usepackage{enumitem}',
    '\\usetikzlibrary{backgrounds}',
    '\\usepackage[scheme=plain]{ctex}',

    # '\\xeCJKsetup{PunctStyle=banjiao}',
    # '\\usepackage{ctexcap}',
    # '\\newfontfamily\\hupo{STXingkai}',

    # '\\newfontfamily\\arialfont{Arial}',
    # '\\newcommand{\\arialft}{\\arialfont\\selectfont}',
    # '\\newfontfamily\\romanfont{Times New Roman}',
    # '\\newcommand{\\romanft}{\\romanfont\\selectfont}',

    # '\\setCJKfamilyfont{hwhp}{STXingkai}',
    # '\\newcommand{\\hupozh}{\\CJKfamily{hwhp}}',
    '\\newcommand{\\fs}[1]{\\fontsize{#1}{0pt}\\selectfont}',
    '\\setCJKmainfont{Microsoft YaHei}',
    '\\CJKsetecglue{\\hskip0.05em plus0.05em minus 0.05em}',
    '\\ctexset{space=true}',
    '\\setmainfont{Microsoft YaHei}',
    # '\\setmainfont{Arial Unicode MS}',
    # '\\setmainfont{FreeSerif}',
]

# Some other not common commands
preamble.extend([
    '''
    \\newcommand\\shadetext[2][]{%
    \\setbox0=\\hbox{{\\special{pdf:literal 7 Tr }#2}}%
    \\tikz[baseline=0]\\path [#1] \\pgfextra{\\rlap{\\copy0}} (0,-\\dp0) rectangle (\\wd0,\\ht0);%
    }

    \\newcommand{\\clr}[2]{%
        \\textcolor{#1}{#2}\\color{white}
    }
    '''
])

begin_doc = ['\\begin{document}\n']
end_doc   = ['\n\\end{document}']


def clearTex(tex_filename):
    with open(tex_filename, 'w'):
        pass

def printCmds(commands):
    global all_tikz_cmds
    if isinstance(commands, str):
        all_tikz_cmds.append(commands)
    elif isinstance(commands, list):
        for line in commands:
            all_tikz_cmds.append(line)

def outputTex(tex_filename,
              preamble_extra=[], compiletex=True, parts=1, threads=1, mergepdf=False, 
              preview=True, engine='xelatex', latexmk=False, aux_dir='latex-temp', out_dir='latex-temp', 
              pdf2png=False, ppi=216, down_scale_factor=2, 
              png2mp4=False, frame_rate=30):
    global all_tikz_cmds

    if tex_filename[-4:] != '.tex':
        tex_filename = ''.join((texfile_name,'.tex'))

    preamble.extend(preamble_extra)

    if parts == 1:
        selected_cmds = all_tikz_cmds

        part_cmds = []
        part_cmds.extend(preamble)
        part_cmds.extend(begin_doc)
        part_cmds.extend(selected_cmds)
        part_cmds.extend(end_doc)


        clearTex(tex_filename)
        with open(tex_filename, 'a', encoding='utf-8') as txf:
            for line in part_cmds:
                print(line, file=txf)
        if compiletex == True:
            compileTex(tex_filename, 
                preview=preview, engine=engine, latexmk=latexmk, aux_dir=aux_dir, out_dir=out_dir,
                pdf2png=pdf2png, ppi=ppi, down_scale_factor=down_scale_factor,
                png2mp4=png2mp4, frame_rate=frame_rate)
    # # I add the multi-thread part to prevent the number of drawing elments exceeding the limits.
    # # I am considering removing this part since it is seldem used and makes the codes ugly.
    # else:
    #     frame_row_bgn = []
    #     frame_row_end = []

    #     frame_cnt, row_num = 0, 0
    #     for row in all_tikz_cmds:
    #         row = row.strip('\n')
    #         if row == '\\begin{tikzpicture}':
    #             frame_row_bgn.append([frame_cnt, row_num])
    #         if row == '\\end{tikzpicture}':
    #             frame_row_end.append([frame_cnt, row_num])
    #             frame_cnt += 1

    #         row_num += 1

    #     parts = min(frame_cnt, parts)

    #     tex_filename_list = []
    #     pdf_filename_list = []
    #     frame_cnt_each_part = ceil(frame_cnt/parts)
    #     bgn_frame_cnt, end_frame_cnt = 0, -1
    #     for i in range(0, parts):
    #         bgn_frame_cnt = end_frame_cnt + 1
    #         if i < parts-1:
    #             end_frame_cnt = bgn_frame_cnt + frame_cnt_each_part - 1
    #         else:
    #             end_frame_cnt = frame_cnt - 1

    #         bgn_row_num = frame_row_bgn[bgn_frame_cnt][1]
    #         end_row_num = frame_row_end[end_frame_cnt][1]

    #         selected_cmds = all_tikz_cmds[bgn_row_num : end_row_num+1]

    #         part_cmds = []
    #         part_cmds.extend(preamble)
    #         part_cmds.extend(begin_doc)
    #         part_cmds.extend(selected_cmds)
    #         part_cmds.extend(end_doc)

    #         tex_filename_tmp = os.path.splitext(tex_filename)[0] + '_{:0>4d}'.format(i+1) + '.tex'
    #         pdf_filename_tmp = os.path.splitext(tex_filename)[0] + '_{:0>4d}'.format(i+1) + '.pdf'
    #         tex_filename_list.append(tex_filename_tmp)
    #         pdf_filename_list.append(pdf_filename_tmp)
    #         clearTex(tex_filename_tmp)
    #         with open(tex_filename_tmp, 'a', encoding='utf-8') as txf:
    #             for line in part_cmds:
    #                 print(line, file=txf)

    #     if compiletex == True:
    #         threads_cnt_max = min(threads, parts)
    #         semlock = threading.BoundedSemaphore(threads_cnt_max)
    #         compile_tex_list=[]
    #         for i in range(0, parts):
    #             semlock.acquire()
    #             tex_filename_tmp = tex_filename_list[i]
    #             compile_tex_tmp = threading.Thread(target=compileTex, args=(tex_filename_tmp,), kwargs={'preview':False, 'pdf2png':pdf2png, 'png2mp4':png2mp4, 'semlock':semlock}) # Need to add missing parameters
    #             compile_tex_list.append(compile_tex_tmp)
    #             compile_tex_tmp.start()
    #             # # Must monitor the last thread, in order to compile all texs before call mergePdf()
    #             # # Ignore other threads to max the utilization of processor
    #             # if i == parts:
    #             #     compile_tex_tmp.join()

    #     if mergepdf == True:
    #         pdf_filename = os.path.splitext(tex_filename)[0] + '.pdf'
    #         mergePdf(input_pdf_list=pdf_filename_list, output_pdf=pdf_filename)
    #         if preview == True:
    #             os.system('sumatrapdf '+ pdf_filename)


def compileTex(tex_filename, 
               preview=True, engine='xelatex', latexmk=False, aux_dir='latex-temp', out_dir='latex-temp',
               pdf2png=False, ppi=216, down_scale_factor=3,
               png2mp4=False, frame_rate=30,
               semlock={}):

    compile_limits = ' -pool-size=7999999 -extra-mem-top=20000000 -extra-mem-bot=20000000'
    absolute_tex_filename = os.path.join(os.getcwd(), tex_filename)

    dir_filename = os.path.splitext(tex_filename)[0]
    pdf_filename = os.path.splitext(tex_filename)[0] + '.pdf'

    # latexmk -xelatex -pv xxx.tex
    if latexmk == True:
        if engine == 'xelatex' or engine == 'x':
            engine_cfg = '-xelatex'
        elif engine == 'pdflatex' or engine == 'pdf' or engine == 'p':
            engine_cfg = '-pdf'
        else:
            engine_cfg = '-xelatex'

        if preview == True:
            preview_cfg = '-pv'
        else:
            preview_cfg = ''

        compile_tool = ' '.join(('latexmk', preview_cfg, compile_limits, engine_cfg, ' '))

        os.system(compile_tool + absolute_tex_filename)

    # xelatex -pool-size=7999999 -extra-mem-top=20000000 -extra-mem-bot=20000000 -recorder xxx.tex
    # start "xxx.pdf"
    else:
        if engine == 'xelatex' or engine == 'x':
            engine_cfg = 'xelatex'
        elif engine == 'pdflatex' or engine == 'pdf' or engine == 'p':
            engine_cfg = 'pdflatex'
        else:
            engine_cfg = 'xelatex'

        if aux_dir == '':
            aux_dir_cfg = ''
            if out_dir == '':
                out_dir_cfg = ''
            else:
                out_dir_cfg = '-out-directory=' + out_dir
        else:
            aux_dir_cfg = '-aux-directory=' + aux_dir
            out_dir_cfg = ''

        compile_tool = ' '.join((engine_cfg, compile_limits, '-recorder', aux_dir_cfg, out_dir_cfg, ' '))
        os.system(compile_tool + absolute_tex_filename)

        os.system('del *.fls')

        if preview == True:
            os.system('start ' + pdf_filename)

    if pdf2png == True:
        if not os.path.exists(dir_filename):
            os.mkdir(dir_filename)
        pdf2png_cmd = 'gswin64c -sDEVICE=pngalpha -r{} -dDownScaleFactor={} -o ./{}/{}_%06d.png {}'\
                        .format(ppi, down_scale_factor, dir_filename, dir_filename, pdf_filename)
        os.system(pdf2png_cmd)

    if png2mp4 == True:
        ffmpeg_path = 'D:/ffmpeg/bin/ffmpeg.exe'
        png2mp4_cmd = '{} -y -framerate {} -i ./{}/{}_%06d.png -pix_fmt yuv420p {}.mp4'\
                        .format(frame_rate, ffmpeg_path, dir_filename, dir_filename, dir_filename)
        os.system(png2mp4_cmd)

    if semlock != {}:
        semlock.release()

def mergePdf(input_pdf_list=[], output_pdf=''):
    gs_cmd = 'gswin64c -dBATCH -dNOPAUSE -sDEVICE=pdfwrite '
    out_cmd = '-o ' + output_pdf + ' '
    input_cmd = ''
    for input_pdf_tmp in input_pdf_list:
        input_cmd = input_cmd + ' ' + input_pdf_tmp
    os.system(gs_cmd + out_cmd + input_cmd)

def beginTikz(empty=False, bgcolor='black', unit='pt'):
    begin_tikz = [
        '\\begin{tikzpicture}',
        '[',
        'x=1{}, y=1{},'.format(unit,unit),
        'background rectangle/.style={{fill={}}},'.format(bgcolor),
        'show background rectangle,',
        # 'scale=1.5',
        ']\n',
    ]

    if empty == True:
        # The following command is to avoid 'Dimension too large' 
        #   if no elment is drawn on the tikzpicture
        begin_tikz.extend([
            '\\path (0, 0) rectangle (1, 1);', 
        ])
    printCmds(begin_tikz)

def endTikz():
    end_tikz = '\n\\end{tikzpicture}\n'
    printCmds(end_tikz)

def setSize(width=1285, height=723, quality='720p', anchor='lb', typex='str'):
    if   typex == 'num':
    # anchor is the center of the origin point of the bounding box
    #   - left right up bottom center
    #   - l,r,u,b, lu, lb, ru, rb, c
        width, height = width, height

    elif typex == 'str':
    # width, height = 1280+5, 720+3
    # width, height = 1920+7, 1080+4
        if   quality == '720p':
            width, height = 1280+5, 720+3
        elif quality == '1080p':
            width, height = 1920+7, 1080+4
        else:
            width, height = 1920+7, 1080+4

    tmp_cmds = [
            '\\path[clip] (0, 0) rectangle ({0:}, {1:});'.format(width, height),
        ]

    printCmds(tmp_cmds)
