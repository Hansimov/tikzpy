## Comparisons of some typical drawing tools

It is hard to properly classify the large number of tools for making **drawings/plots/charts/diagrams/graphs/graphics/images/illustrations/visualizations/typesettings** to independent groups. To make it simple, I use "drawing tools" in this document to refer to tools designed for all kinds of tasks emphasized above. 

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
        * converting .ps to bitmaps takes a long time?
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

* Adobe Indesign

### Graphics
* .dot
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
      * Good at geometry and plotting
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

* Openframeworks
  * Pros:
    * Tasks:
      * Large number of useful functions
      * Support multiple media
    * Solutions:
      * Fast
      * Open source
      * Rich API references
      * Large number of users and active communities
  * Cons:
    * Tasks:
      * Lack of support for LaTeX typesettings
      * Must put all logics into a loop
        * This is not natural for non-linear drawings 
    * Solutions:
      * C++ is not convinient
      * Need to recompile when file changes
      * Must develop with IDE
      * Intermediate files are large (in .vs)
      * Tutorials and documents are not really systematic

* Processing/processing.py
  * Similar to openframeworks, just several differences:
  * Pros:
    * Tasks:
      * Large number of libraries and extensions
    * Solutions:
      * Large number of tutorials and documents
  * Cons:
    * Tasks:
      * ...
    * Solutions:
      * Java is still not convenient enough

* Cairo/**Pycairo**/Gizeh/cairocffi

* pango

* paper.js/raphael.js/p5.js

* **manim**
  * Pros:
    * Tasks:
      * Support LaTeX
      * Designed for math animations
    * Solutions:
      * Open source
      * Pythonic
  * Cons:
    * Tasks:
      * Few functions
      * Must generate videos and no real-time previews
      * Not suitable for drawing large number of elements
    * Solutions:
      * Troublesome to install and configure
      * Really few tutorials or documents, almost none
      * None community and few users by far

* Adobe Illustrator
* Dia
* Inkscape

### Graphics Interfaces
* DirectX
* **OpenGL**
* WebGL
* Qt/PyQt
* Gtk+

### Data Visualizations / Plots
* D3.js
  * Pros:
    * Tasks:
      * All kinds of data visualizations and plots
      * Interactive
    * Solutions:
      * Open source
      * Large number of tutorials, examples, documents and API references
      * Large number of users and active community
      * Flexible and extendable
  * Cons:
    * Tasks:
      * Cannot export images in large numbers
        * It is almost impossible to create high-quality videos without each frame exported, except using screen recorders
      * Not designed for typesettings and motion graphics
      * Lack of support for complicated LaTeX
    * Solutions:
      * Not suitable for drawing large number of elements
      * Has most drawbacks of the tools based on JavaScript

* matplotlib
  * Similar to D3.js, just several differences
  * Pros:
    * Tasks:
      * ...
    * Solutions:
      * Pythonic
  * Cons:
    * Tasks:
      * Lack support for animations (actually can do, but the methods are really strange)
    * Solutions:
      * Buggy, sometimes even dead
      * Not able to plot large number of elements
      * The design is not elegant

* gnuplot/gnuplot-py
* vispy
* PyQtGraph
* R
* Mathematica
* MATLAB

### Schematic Diagrams
* Office Visio
* XMind/MindManager
* UML

### Image Processing
* Pillow
* Adobe Photoshop

