## Comparisons of some typical drawing tools

It is hard to properly classify the large number of tools for making **drawings/plots/graphs/graphics/images/illustrations/visualizations/typesettings** to independent groups. To make it simple, I use "drawing tools" in this document to refer to tools designed for all kinds of tasks emphasized above. 

What standards should we choose to compare these tools?
By the tasks which the tool is designed for?
By the programming languages (or domain-specific languages) which develop or used by the tools?
By the weight or size of the tools?
...

Do not fall into details. There are only two important questions need to be considered: **"What does it do"** and **"How does it do"**. "What" focuses the tasks and "How" focuses on the solutions. For example, "it supports different fonts" and "it can decorate paths" are "what", while "it is fast" and "it uses python as programming language" are "how".

Here I list some typical drawing tools by the "what" of them, which means they are ordered by the tasks they are used for.
Some tools may be used for more than one task, but I will only put them into the groups where they do the best jobs.

The pros and cons may not be right. These are just my personal opinions. Some tools may have same pros or cons, so I only write down the most obvious aspects.

I emphasize several outstanding ones and will have deep researches on them later to assist the designs of my tool.


* Typesetting
  * PostScript/MetaPost:
    * Pros:
      * Tasks:
        * Powerful
          * Turing-complete
          * Good at font processing
      * Solutions:
        * Grammar is concise
        * Real-time feedback of changes
    * Cons:
      * Tasks:
        * Only supports .ps files
          * converting .ps to bitmaps takes a long time
          * .ps files do not support transparency/opacity
        * Few existed extended packages, although it is powerful
      * Solutions:
        * Need to learn a new language
        * Tutorials are not enough besides official documentations
          * This also means it is hard to get others' help compared to those popular tools
        * Hard to debug

  * **TikZ/PGF**:
    * Pros:
      * Tasks:
        * Powerful
          * Graphs, illustraions, data visualizations and so on
          * Supports math formulas and all kinds of symbols
          * Seamless connection with texts
        * Flexible
          * Large number of libraries and packages based on it
      * Solutions:
        * Excellent tutorials, examples and documents
        * Active communities on TeX Stack Exchange 
        * Grammar is intuitive
    * Cons:
      * Tasks:
        * Only supports PDF and realated file types
          * converting .pdf to bitmaps takes a long time
        * Do not support real 3D by far
      * Solutions:
        * Need to recompile everytime when the file changes
        * Hard to program in TeX since it is based on "macros"

   * PSTricks
     * Similar to TikZ/PGF, just some small differences:
     * Pros:
       * Tasks:
         * Can access the full power of PostScript  
         * Have some useful packages and there have not been good alternatives in TikZ  
         * Supports real 3D
       * Solutions:
         * ...
     * Cons:
       * Tasks:
         * ...
       * Solutions:
         * Tutorials and documents are not as good
         * Slower than TikZ/PGF
         * Need to learn a new language

* Graphics
**Asymptote**
JSXGraph
vispy
Cairo/Gizeh/Pycairo/cairocffi
paper.js/raphael.js
Openframeworks
Processing/**p5.js**/processing.py

* Graphics Interfaces
DirectX
**OpenGL**
WebGL
Qt/PyQt

* Data Visualizations / Plotting 
gnuplot/gnuplot-py
**matplotlib**
PyQtGraph
D3.js
R
Mathematica
MATLAB

* Images
Pillow

