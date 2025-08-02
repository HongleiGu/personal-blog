---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# 5.1:

```prolog
% teaches(?PersonID, ?CourseID)
teaches(tk106, 70043).

% person(?ID, ?First, ?Last)
person(tk106, 'Timothy', 'Kimber').

% role(?PersonID, ?Role)
role(tk106, 'TF').
```

**Given a file of ground clauses for the predicates illustated above, define a predicate ra_lecturer(-First, -Last) that succeeds when First and Last are the names of a Research Associate(role "RA") who teaches any course. Use anonymous vairables where appropriate**

```prolog
ra_lecture(First, Last) :-
  person(ID, First, Last),
  role(ID, 'RA'),
  teaches(ID,_).
```

# 5.2:

```prolog
transform(Image, gray, Transformed):
  copy_pixels(Image, Copy),
  colors_to_black(Copy, Gray),
  save_transformed_image(Gray, Transformed).
transform(Image, reflect, Transformed):
  store_pixels(Image, Buffer),
  pad_image(Buffer, SquareImage),
  copy_pixels(SquareImage, Copy),
  reverse_pixels(Copy, Reversed),
  save_transformed_image(Reversed, Transformed).
transform(Image, blur, Transformed):
  store_pixels(Image, Buffer),
  pad_image(Buffer, SquareImage),
  copy_pixels(SquareImage, Copy),
  blur_pixels(Copy, Blurred),
  save_transformed_image(Blurred, Transformed).
```

**Refactor the program above to reduce the amount of repeated code.**

```prolog
transform_helper(Image, _, Transformed):
  store_pixels(Image, Buffer),
  pad_image(Buffer, SquareImage),
  copy_pixels(SquareImage, Copy),

transform(Image, gray, Transformed):
  copy_pixels(Image, Copy),
  colors_to_black(Copy, Gray),
  save_transformed_image(Gray, Transformed).

transform(Image, reflect, Transformed):
  transform_helper(Image, reflect, Transformed),
  reverse_pixels(Copy, Reversed),
  save_transformed_image(Reversed, Transformed).

transform(Image, blur, Transformed):-
  transform_helper(Image, blur, Transformed),
  blur_pixels(Copy, Blurred),
  save_transformed_image(Blurred, Transformed).
```

# 5.3:

**Write a tail recursive program to implement mult(+X, +Y, -Z), where X >= 0 is an integer, Y >= 0 is an integer and Z is multiplied by Y, You may use the + operator, but not the * operator**

```prolog
multi(X, Y+1, Z+X) :-
  multi(X,Y,Z).

multi(X+1, Y, Z+Y) :-
  multi(X,Y,Z).

multi(0, _, 0).
multi(_, 0, 0).
multi(1, Y, Y).
multi(X, 1, X).
```


# 5.4

**Write a program lucky(+N) that suceeds if N is 70043 and fails if N is any other number**

```prolog
lucky(70043).
```