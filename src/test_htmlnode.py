import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", "Click me", props={"href": "https://www.boot.dev", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.boot.dev" target="_blank"'
        )

    def test_init(self):
        node = HTMLNode(
            "a",
            "Click me",
            children=[HTMLNode("p", "Text", props={"href": "https://www.boot.dev"})],
        )
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me")
        self.assertIsNone(node.props)
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[0].value, "Text")
        self.assertEqual(node.children[0].props, {"href": "https://www.boot.dev"})
        self.assertIsNone(node.children[0].children)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
