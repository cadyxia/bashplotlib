# test.py
from bashplotlib.scatterplot import _plot_scatter
import unittest

class TestScatterPlot(unittest.TestCase):
  def test_no_points(self):
    self.assertEqual(_plot_scatter([], [], 10, "x",
                                  "My Test Graph", "default", "My X Axis", "My Y Axis"), 
                    """  +------------------------+\n  |     My Test Graph      |
  +------------------------+
  +------------------------+
M |           |            |
y |           |            |
  |           |            |
Y |           |            |
  |           |            |
A | - - - - - o - - - - -  |
x |           |            |
i |           |            |
s |           |            |
  |           |            |
  |           |            |
  +------------------------+
  My X Axis""")
    
  def test_points(self):
    self.assertEqual(_plot_scatter([-10, -3, 20,30], [-10, 6, 20,-2], 10, "*",
                                  "Points!", "default", "Something x", "Another y"), 
                    """  +--------------------------+\n  |         Points!          |
  +--------------------------+
  +--------------------------+
A |       |           *      |
n |       |                  |
o |       |                  |
t |       |                  |
h |       |                  |
e |     * |                  |
r |       |                  |
  | - - - o - - - - - - - -  |
y |       |                  |
  |       |               *  |
  |       |                  |
  | *     |                  |
  +--------------------------+
  Something x""")

  def test_points_on_axes(self):
    self.assertEqual(_plot_scatter([0, -10, 0, 20,0], [0, 0, 6, 0,-2], 10, "#",
                                  "Points!", "default", "x", "y"),
                    """  +--------------------------+\n  |         Points!          |
  +--------------------------+
  +--------------------------+
y |         #                |
  |         |                |
  |         |                |
  |         |                |
  |         |                |
  |         |                |
  |         |                |
  |         |                |
  | # - - - # - - - - - - #  |
  |         |                |
  |         |                |
  |         #                |
  +--------------------------+
  x""")

if __name__ == "__main__":
  unittest.main()
