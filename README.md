# triforce
proof that i can write a program that generates a triforce for any given height

### usage

usage: ```triangle.py <level> <scale> [substance]```

```<level>``` is how many layers the triforce has.  For example, a Triforce proper is of level 2 because it has 2 layers (or rows) of triangles. ```<scale>``` is how big each individual triangle that makes up the triforce will be. ```substance``` is optional and it's what the triforce is made out of.  default is ▲, but it can be a character, word, or emoji so long as it doesn't have spaces in it
  

### example

```$ python triforce.py 4 3```

Output:

```
printing a 4-force of scale 3
           ▲
          ▲▲▲
         ▲▲▲▲▲
        ▲     ▲
       ▲▲▲   ▲▲▲
      ▲▲▲▲▲ ▲▲▲▲▲
     ▲     ▲     ▲
    ▲▲▲   ▲▲▲   ▲▲▲
   ▲▲▲▲▲ ▲▲▲▲▲ ▲▲▲▲▲
  ▲     ▲     ▲     ▲
 ▲▲▲   ▲▲▲   ▲▲▲   ▲▲▲
▲▲▲▲▲ ▲▲▲▲▲ ▲▲▲▲▲ ▲▲▲▲▲

```

``` $ python triforce.py 2 3 hello```

Output:

```printing a 2-force of scale 3 made up of hello's
                         hello
                    hellohellohello
               hellohellohellohellohello
          hello                         hello
     hellohellohello               hellohellohello
hellohellohellohellohello     hellohellohellohellohello
```
