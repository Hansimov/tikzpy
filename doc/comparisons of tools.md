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

The pros and cons may not be really objective. These are just my personal opinions. Some tools may have same pros or cons with others, so I only write down the most obvious aspects. It is necessary to notice that the referred cons are usually more useful than pros, as we always take the pros as granted, and the cons are indeed the motives to improve original tools or create new ones. And in many cases, the pros may be cons from another perspective.

I emphasize several outstanding ones and will have deep researches on them later to assist the designs of my tool.


### Typesettings
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
      * Need to learn a new language

* PSTricks
  * Similar to TikZ/PGF, just several differences:
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
      * Sometimes slower than TikZ/PGF

### Graphics
* **Asymptote**
  * Pros:
    * Tasks:
      * Supports LaTeX labels
      * Support .ps and other types which ImageMagick can produce
      * Support real 3D
      * Can access the power of C++
      * Have a GUI
    * Solutions:
      * Open source
      * Still active and maintained
      * Fast
      * Large number of examples
  * Cons:
    * Tasks:
      * ...
    * Solutions:
      * Need to learn a new language
      * Hard to debug
      * Tutorials and documents are not enough
      * Few users and small communities
      * C++ is heavy and hard to use, compared to other programming languages like Python

* JSXGraph
  * Pros:
    * Tasks:
      * Good at geometry
      * Interactive
    * Solutions:
      * Light-weight
      * Open source
  * Cons:
    * Tasks:
      * Do not support other kinds of drawings
      * Cannot export images in large numbers
        * This is the drawback of all JavaScript-based tools
        * It is almost impossible to create high-quality videos without each frame exported, except using screen recorders
    * Solutions:
      * ...

* Cairo/Gizeh/Pycairo/cairocffi
  * Pros:
    * Tasks:
    * Solutions:
  * Cons:
    * Tasks:
    * Solutions:

* Openframeworks
  * Pros:
    * Tasks:
    * Solutions:
  * Cons:
    * Tasks:
    * Solutions:
* paper.js/raphael.js/p5.js
  * Pros:
    * Tasks:
    * Solutions:
  * Cons:
    * Tasks:
    * Solutions:
* Processing/processing.py
  * Pros:
    * Tasks:
    * Solutions:
  * Cons:
    * Tasks:
    * Solutions:


**manim**

### Graphics Interfaces
* DirectX
* **OpenGL**
* WebGL
* Qt/PyQt

### Data Visualizations / Plotting 
* gnuplot/gnuplot-py
* **matplotlib**
  * Pros:
    * Tasks:
    * Solutions:
  * Cons:
    * Tasks:
    * Solutions:
* vispy
* PyQtGraph
* D3.js
  * Pros:
    * Tasks:
    * Solutions:
  * Cons:
    * Tasks:
    * Solutions:
* R
* Mathematica
* MATLAB

### Image Processing
* Pillow



