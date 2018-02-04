#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nose.tools import assert_equal, assert_true, raises, assert_is_none
from ODBPy.StandardSymbols import *
from ODBPy.Structures import HolePlating

class TestStandardSymbolParsing(object):
    def testRound(self):
        assert_equal(Round(40.), Round.Parse("r40"))
        assert_equal(Round(3.5), Round.Parse("r3.5"))
        assert_is_none(Round.Parse("rabc"))
        assert_is_none(Round.Parse("s3.5"))

    def testSquare(self):
        assert_equal(Square(40.), Square.Parse("s40"))
        assert_equal(Square(3.5), Square.Parse("s3.5"))
        assert_is_none(Square.Parse("sabc"))
        assert_is_none(Square.Parse("r3.5"))

    def testRectangle(self):
        assert_equal(Rectangle(60., 30.), Rectangle.Parse("rect60x30"))
        assert_equal(Rectangle(1., 2), Rectangle.Parse("rect1x2"))
        assert_equal(Rectangle(5.1, 3.33), Rectangle.Parse("rect5.1x3.33"))
        assert_is_none(Rectangle.Parse("rabc"))
        assert_is_none(Rectangle.Parse("r3.5"))
        assert_is_none(Rectangle.Parse("r1x2x3"))

    def testRoundedRectangle(self):
        assert_equal(RoundedRectangle(60., 30., 5, [1, 3]), RoundedRectangle.Parse("rect60x30xr5x13"))
        assert_equal(RoundedRectangle(60., 30., 5, [1, 2, 3, 4]), RoundedRectangle.Parse("rect60x30xr5"))
        assert_is_none(RoundedRectangle.Parse("rectabc"))
        assert_is_none(RoundedRectangle.Parse("rect3.5"))
        assert_is_none(RoundedRectangle.Parse("rect1x2x3"))
        assert_is_none(RoundedRectangle.Parse("rect1x2xc3"))

    def testChamferedRectangle(self):
        assert_equal(ChamferedRectangle(60., 30., 5, [1, 3]), ChamferedRectangle.Parse("rect60x30xc5x13"))
        assert_equal(ChamferedRectangle(60., 30., 5, [1, 2, 3, 4]), ChamferedRectangle.Parse("rect60x30xc5"))
        assert_is_none(ChamferedRectangle.Parse("rectabc"))
        assert_is_none(ChamferedRectangle.Parse("rect3.5"))
        assert_is_none(ChamferedRectangle.Parse("rect1x2x3"))
        assert_is_none(ChamferedRectangle.Parse("rect1x2xr3"))

    def testOval(self):
        assert_equal(Oval(60., 30.), Oval.Parse("oval60x30"))
        assert_equal(Oval(1., 2), Oval.Parse("oval1x2"))
        assert_equal(Oval(5.1, 3.33), Oval.Parse("oval5.1x3.33"))
        assert_is_none(Oval.Parse("ovalabc"))
        assert_is_none(Oval.Parse("oval3.5"))

    def testDiamond(self):
        assert_equal(Diamond(60., 30.), Diamond.Parse("di60x30"))
        assert_equal(Diamond(1., 2), Diamond.Parse("di1x2"))
        assert_equal(Diamond(5.1, 3.33), Diamond.Parse("di5.1x3.33"))
        assert_is_none(Diamond.Parse("diabc"))
        assert_is_none(Diamond.Parse("di3.5"))

    def testOctagon(self):
        assert_equal(Octagon(60., 60., 20.), Octagon.Parse("oct60x60x20"))
        assert_equal(Octagon(60., 30., 20.), Octagon.Parse("oct60x30x20"))
        assert_equal(Octagon(1., 2.0, 3.0), Octagon.Parse("oct1.0x2.0x3.0"))
        assert_equal(Octagon(5.1, 3.33, 61.2), Octagon.Parse("oct5.1x3.33x61.2"))
        assert_is_none(Octagon.Parse("oct60x60"))
        assert_is_none(Octagon.Parse("oval3.5"))

    def testRoundDonut(self):
        assert_equal(RoundDonut(60, 30), RoundDonut.Parse("donut_r60x30"))
        assert_equal(RoundDonut(3.5, 2.5), RoundDonut.Parse("donut_r3.5x2.5"))
        assert_is_none(RoundDonut.Parse("donut1x2"))
        assert_is_none(RoundDonut.Parse("r3.5"))
        assert_is_none(RoundDonut.Parse("donut_r1x2x3"))

    def testSquareDonut(self):
        assert_equal(SquareDonut(60, 30), SquareDonut.Parse("donut_s60x30"))
        assert_equal(SquareDonut(3.5, 2.5), SquareDonut.Parse("donut_s3.5x2.5"))
        assert_is_none(SquareDonut.Parse("donut_r1x2"))
        assert_is_none(SquareDonut.Parse("r3.5"))
        assert_is_none(SquareDonut.Parse("donut_s1x2x3"))

    def testSquareRoundDonut(self):
        assert_equal(SquareRoundDonut(10, 8), SquareRoundDonut.Parse("donut_sr10x8"))
        assert_equal(SquareRoundDonut(60, 30), SquareRoundDonut.Parse("donut_sr60x30"))
        assert_equal(SquareRoundDonut(3.5, 2.5), SquareRoundDonut.Parse("donut_sr3.5x2.5"))
        assert_is_none(SquareRoundDonut.Parse("donut_r1x2"))
        assert_is_none(SquareRoundDonut.Parse("r3.5"))
        assert_is_none(SquareRoundDonut.Parse("donut_s1x2x3"))

    def testRoundedSquareDonut(self):
        assert_equal(RoundedSquareDonut(10, 8, 2, [1,2,3,4]), RoundedSquareDonut.Parse("donut_s10x8xr2"))
        assert_is_none(RoundedSquareDonut.Parse("donut_r1x2"))
        assert_is_none(RoundedSquareDonut.Parse("r3.5"))
        assert_is_none(RoundedSquareDonut.Parse("donut_s1x2x3"))

    def testRectangleDonut(self):
        assert_equal(RectangleDonut(8, 6, 1), RectangleDonut.Parse("donut_rc8x6x1"))
        assert_is_none(RectangleDonut.Parse("donut_rc1x2"))
        assert_is_none(RectangleDonut.Parse("donut_rc1x2x3x4"))
        assert_is_none(RectangleDonut.Parse("r3.5"))

    def testRoundedRectangleDonut(self):
        assert_equal(RoundedRectangleDonut(10, 7, 1, 2, [1,2,3,4]), RoundedRectangleDonut.Parse("donut_rc10x7x1xr2"))
        assert_is_none(RoundedRectangleDonut.Parse("donut_rc1x2"))
        assert_is_none(RoundedRectangleDonut.Parse("donut_rc1x2x3"))
        assert_is_none(RoundedRectangleDonut.Parse("donut_rc1x2x3x4x"))
        assert_is_none(RoundedRectangleDonut.Parse("donut_rc1x2x3x4x5"))
        assert_is_none(RoundedRectangleDonut.Parse("donut_rc1x2x3x4x5x6"))
        assert_is_none(RoundedRectangleDonut.Parse("r3.5"))
        assert_is_none(RoundedRectangleDonut.Parse("donut_s1x2x3"))

    def testOvalDonut(self):
        assert_equal(OvalDonut(5, 3, .5), OvalDonut.Parse("donut_o5x3x0.5"))
        assert_is_none(OvalDonut.Parse("donut_o1x2"))
        assert_is_none(OvalDonut.Parse("donut_o1x2x3x4"))
        assert_is_none(OvalDonut.Parse("r3.5"))

    def testHorizontalHexagon(self):
        assert_equal(HorizontalHexagon(60, 60, 20), HorizontalHexagon.Parse("hex_l60x60x20"))
        assert_is_none(HorizontalHexagon.Parse("hex_l1x2"))
        assert_is_none(HorizontalHexagon.Parse("hex_l1x2x3x4"))
        assert_is_none(HorizontalHexagon.Parse("r3.5"))

    def testVerticalHexagon(self):
        assert_equal(VerticalHexagon(60, 60, 20), VerticalHexagon.Parse("hex_s60x60x20"))
        assert_is_none(VerticalHexagon.Parse("hex_s1x2"))
        assert_is_none(VerticalHexagon.Parse("hex_s1x2x3x4"))
        assert_is_none(VerticalHexagon.Parse("r3.5"))

    def testButterfly(self):
        assert_equal(Butterfly(60), Butterfly.Parse("bfr60"))

    def testSquareButterfly(self):
        assert_equal(SquareButterfly(60), SquareButterfly.Parse("bfs60"))

    def testTriangle(self):
        assert_equal(Triangle(30, 60), Triangle.Parse("tri30x60"))

    def testHalfOval(self):
        assert_equal(HalfOval(30, 60), HalfOval.Parse("oval_h30x60"))

    def testRoundThermalRounded(self):
        assert_equal(RoundThermalRounded(60,40,45,4,10),
            RoundThermalRounded.Parse("thr60x40x45x4x10"))

    def testRoundThermalSquared(self):
        assert_equal(RoundThermalSquared(60,40,45,4,10),
            RoundThermalSquared.Parse("ths60x40x45x4x10"))

    def testSquareThermal(self):
        assert_equal(SquareThermal(60,40,45,4,10),
            SquareThermal.Parse("s_ths60x40x45x4x10"))

    def testSquareThermalOpenCorners(self):
        assert_equal(SquareThermalOpenCorners(60,40,45,4,10),
            SquareThermalOpenCorners.Parse("s_tho60x40x45x4x10"))

    def testSquareRoundThermal(self):
        assert_equal(SquareRoundThermal(60,40,45,4,10),
            SquareRoundThermal.Parse("sr_ths60x40x45x4x10"))

    def testRectangularThermal(self):
        assert_equal(RectangularThermal(60,40,45,4,10,10),
            RectangularThermal.Parse("rc_ths60x40x45x4x10x10"))

    def testRectangularThermalOpenCorners(self):
        assert_equal(RectangularThermalOpenCorners(60,40,45,4,10,10),
            RectangularThermalOpenCorners.Parse("rc_tho60x40x45x4x10x10"))

    def testRoundedSquareThermal(self):
        assert_equal(RoundedSquareThermal(40,30,90,4,4,4,[1,2,3,4]),
            RoundedSquareThermal.Parse("s_ths40x30x90x4x4xr4"))

    def testRoundedSquareThermalOpenCorners(self):
        assert_equal(RoundedSquareThermalOpenCorners(40,30,90,4,4,4,[1,2,3,4]),
            RoundedSquareThermalOpenCorners.Parse("s_tho40x30x90x4x4xr4"))

    def testRoundedRectangleThermal(self):
        assert_equal(RoundedRectangleThermal(10,7,90,4,2,1,2,[1,2,3,4]),
            RoundedRectangleThermal.Parse("rc_ths10x7x90x4x2x1xr2"))

    def testRoundedRectangleThermalOpenCorners(self):
        assert_equal(RoundedRectangleThermalOpenCorners(10,7,90,4,2,1,2,[1,2,3,4]),
            RoundedRectangleThermalOpenCorners.Parse("rc_tho10x7x90x4x2x1xr2"))

    def testOvalThermal(self):
        assert_equal(OvalThermal(5,3,.5,90,4,1),
            OvalThermal.Parse("o_ths5x3x0.5x90x4x1"))

    def testOvalThermalOpenCorners(self):
        assert_equal(OvalThermalOpenCorners(5,3,.5,90,4,1),
            OvalThermalOpenCorners.Parse("o_tho5x3x0.5x90x4x1"))

    def testEllipse(self):
        assert_equal(Ellipse(30, 60), Ellipse.Parse("el30x60"))

    def testMoire(self):
        assert_equal(Moire(5,10,4,4,100,0),
            Moire.Parse("moire5x10x4x4x100x0"))

    def testHole(self):
        assert_equal(Hole(50,HolePlating.Plated,4,5),
            Hole.Parse("hole50xpx4x5"))
        assert_equal(Hole(50,HolePlating.NonPlated,4,5),
            Hole.Parse("hole50xnx4x5"))
        assert_equal(Hole(50,HolePlating.Via,4,5),
            Hole.Parse("hole50xvx4x5"))




