# Python Collections Table

Jey Lofton — FSDI 108

A comparison of the four main Python collections.

| Data Structure | Syntax Example       | Ordered | Mutable | Allows Duplicates        | Access Method       |
| -------------- | -------------------- | ------- | ------- | ------------------------ | ------------------- |
| **List**       | `[10, 20, 30]`       | Yes     | Yes     | Yes                      | `list[0]`           |
| **Dictionary** | `{"a": 10, "b": 20}` | Yes     | Yes     | No (keys must be unique) | `dict["a"]`         |
| **Set**        | `{10, 20, 30}`       | No      | Yes     | No                       | Loop or `10 in set` |
| **Tuple**      | `(10, 20, 30)`       | Yes     | No      | Yes                      | `tuple[0]`          |

## Notes

- **Ordered** means the items stay in the position you put them. A set does not keep
  order, so you cannot ask for "the first item."
- **Mutable** means you can change it after you create it. A tuple is the only one of
  the four that is immutable — once it is made, it is locked.
- **Allows duplicates**: a dictionary can repeat _values_, but every _key_ must be
  unique. Assigning to a key that already exists overwrites it instead of adding it.
- **Access method**: lists and tuples use a position (index), dictionaries use a key,
  and sets use neither — you loop through them or check membership with `in`.
