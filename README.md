# tree_preety_print

```python
tree = Tree(
    value="1",
    children=[
        Tree(
            value="1.1",
            children=[
                Tree(value="1.1.1"),
                Tree(value="1.1.2"),
            ]
        ),
        Tree(
            value="1.2",
            children=[
                Tree(value="1.2.1"),
                Tree(value="1.2.2"),
                Tree(value="1.2.3"),
            ]
        )
    ]
)

pretty_print(tree)
```

```text
 └── 1
    ├── 1.1
    │  ├── 1.1.1
    │  └── 1.1.2
    └── 1.2
       ├── 1.2.1
       ├── 1.2.2
       └── 1.2.3
```