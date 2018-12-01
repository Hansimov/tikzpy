## Tasks

"Tasks" are the answer of the question "what does this tool do", or to be more accurate, "what is it designed for".

### What is this tool designed for

To a great extent, this tool is something like "TikZ written in Python". What I intend to do is just patch the defects of TikZ mentioned before. These defects are few but fatal. Fortunately (or unfortunately), all of the defects are not about "tasks" but "solutions". Thus, I will discuss this in the "Solutions" part.

What this tool can do is what TikZ can do. And I only focus on these tasks:

* Idea-Driven Drawings: Schematic diagrams
    * Record or present ideas
    * Used in tutorials and open courses
    * Support a little bit of (but enough) LaTeX
    * Dynamic and easy to export to videos/gifs
* Motion Graphics

### What is this tool not designed for
People always want one tool that can do as much as possible, and this is the primitive desire which promotes the development of softwares. However, in many cases, the more important question is "what we **do not** want", especially for a newborn project.

Therefore, here I list what this tool is not designed for (at least by far):

* Data Visualizations / Plots / Data-Driven Diagrams
* Multimedia Interaction
* ...

## Solutions

### What is the way this tool works

"Solutions" are the answer of the question "How does this tool do".

* Fast
* Extendable
* Neat
    * Renderer can be separated from Editor
    * (IDE can attract more users and is convinient, but I prefer text editors for its flexibility)
    * (So the what the software really does is designing a domain-specific language and implementing a corresponding renderer)


### What is not the way this tool works

* WYSIWYG and Drag&Drop like visio/photoshop/inkscape:
    * To complicated for me for now
    * Hard to map casual handrawn objects to texts/commands
    * Can be partly compensated by some small tools: coordinate locator, color picker, frameworks, ...
* 