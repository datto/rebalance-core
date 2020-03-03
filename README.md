
Implements a simple resource rebalancing algorithm.

By implementing the `Node` and `Item` classes, you can use the `plan` method to find what items to move to what nodes to improve the node balance. Items can override the `can_move_to` method to determine whether the item can move to a particular node, to enforce, for example, only one replica per host.

The planning algorithm is a fairly simplistic greedy brute force search, which isn't super performant or optimal, but is flexible and gets decent results.
