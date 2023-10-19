/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : M-2016.12-SP1
// Date      : Tue May 16 20:23:08 2023
/////////////////////////////////////////////////////////////


module dff_0 ( clk, q, d );
  input clk, d;
  output q;


  DFFX1_RVT q_reg ( .D(d), .CLK(clk), .Q(q) );
endmodule


module dff_1 ( clk, q, d );
  input clk, d;
  output q;


  DFFX1_RVT q_reg ( .D(d), .CLK(clk), .Q(q) );
endmodule


module dff_2 ( clk, q, d );
  input clk, d;
  output q;


  DFFX1_RVT q_reg ( .D(d), .CLK(clk), .Q(q) );
endmodule


module dff_3 ( clk, q, d );
  input clk, d;
  output q;


  DFFX1_RVT q_reg ( .D(d), .CLK(clk), .Q(q) );
endmodule


module dff_4 ( clk, q, d );
  input clk, d;
  output q;


  DFFX1_RVT q_reg ( .D(d), .CLK(clk), .Q(q) );
endmodule


module dff_5 ( clk, q, d );
  input clk, d;
  output q;


  DFFX1_RVT q_reg ( .D(d), .CLK(clk), .Q(q) );
endmodule


module s386 ( GND, VDD, CK, v0, v1, v13_D_10, v13_D_11, v13_D_12, v13_D_6, 
        v13_D_7, v13_D_8, v13_D_9, v2, v3, v4, v5, v6 );
  input GND, VDD, CK, v0, v1, v2, v3, v4, v5, v6;
  output v13_D_10, v13_D_11, v13_D_12, v13_D_6, v13_D_7, v13_D_8, v13_D_9;
  wire   v12, v11, v10, v9, v8, v7, Lv13_D_12, Lv13_D_11, Lv13_D_10, Lv13_D_9,
         Lv13_D_8, Lv13_D_7, Lv13_D_6, Lv13_D_5, Lv13_D_4, Lv13_D_3, Lv13_D_2,
         Lv13_D_1, Lv13_D_0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12,
         n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25, n26,
         n27, n28, n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39, n40,
         n41, n42, n43, n44, n45, n46, n47, n48, n49, n50, n51, n52, n53, n54,
         n55, n56, n57, n58, n59, n60, n61, n62, n63, n64, n65, n66, n67, n68;
  assign v13_D_12 = Lv13_D_12;
  assign v13_D_11 = Lv13_D_11;
  assign v13_D_10 = Lv13_D_10;
  assign v13_D_9 = Lv13_D_9;
  assign v13_D_8 = Lv13_D_8;
  assign v13_D_7 = Lv13_D_7;
  assign v13_D_6 = Lv13_D_6;

  dff_0 DFF_0 ( .clk(CK), .q(v12), .d(Lv13_D_5) );
  dff_5 DFF_1 ( .clk(CK), .q(v11), .d(Lv13_D_4) );
  dff_4 DFF_2 ( .clk(CK), .q(v10), .d(Lv13_D_3) );
  dff_3 DFF_3 ( .clk(CK), .q(v9), .d(Lv13_D_2) );
  dff_2 DFF_4 ( .clk(CK), .q(v8), .d(Lv13_D_1) );
  dff_1 DFF_5 ( .clk(CK), .q(v7), .d(Lv13_D_0) );
  AO21X1_RVT U74 ( .A1(n5), .A2(n61), .A3(n6), .Y(n24) );
  OA22X1_RVT U75 ( .A1(v2), .A2(n66), .A3(v3), .A4(n61), .Y(n26) );
  OA21X1_RVT U76 ( .A1(n61), .A2(n67), .A3(n63), .Y(n60) );
  OR2X1_RVT U77 ( .A1(n13), .A2(v1), .Y(n50) );
  NBUFFX2_RVT U78 ( .A(n68), .Y(n61) );
  NAND3X0_RVT U79 ( .A1(n7), .A2(n11), .A3(v2), .Y(n38) );
  INVX1_RVT U80 ( .A(v8), .Y(n11) );
  INVX1_RVT U81 ( .A(v11), .Y(n62) );
  INVX1_RVT U82 ( .A(n62), .Y(n63) );
  INVX1_RVT U83 ( .A(v5), .Y(n17) );
  INVX1_RVT U84 ( .A(v4), .Y(n16) );
  NOR3X0_RVT U85 ( .A1(v10), .A2(v9), .A3(n50), .Y(n35) );
  NAND2X0_RVT U86 ( .A1(v2), .A2(n12), .Y(n33) );
  INVX1_RVT U87 ( .A(v3), .Y(n15) );
  NAND3X0_RVT U88 ( .A1(n37), .A2(n67), .A3(n38), .Y(n34) );
  INVX1_RVT U89 ( .A(v9), .Y(n10) );
  INVX1_RVT U90 ( .A(v12), .Y(n4) );
  AND3X1_RVT U91 ( .A1(n7), .A2(n15), .A3(v8), .Y(n21) );
  INVX1_RVT U92 ( .A(v1), .Y(n14) );
  AND2X1_RVT U93 ( .A1(n4), .A2(n10), .Y(n20) );
  INVX1_RVT U94 ( .A(v10), .Y(n8) );
  INVX1_RVT U95 ( .A(v0), .Y(n13) );
  NAND2X0_RVT U96 ( .A1(n49), .A2(n8), .Y(n41) );
  AO22X1_RVT U97 ( .A1(n20), .A2(n50), .A3(n51), .A4(n9), .Y(n49) );
  INVX1_RVT U98 ( .A(n42), .Y(n9) );
  NAND3X0_RVT U99 ( .A1(n63), .A2(n35), .A3(n2), .Y(n28) );
  INVX1_RVT U100 ( .A(n36), .Y(n2) );
  AND2X1_RVT U101 ( .A1(n35), .A2(n4), .Y(n23) );
  OAI22X1_RVT U102 ( .A1(n63), .A2(n36), .A3(v12), .A4(n54), .Y(n53) );
  OA22X1_RVT U103 ( .A1(n55), .A2(n62), .A3(n63), .A4(n56), .Y(n54) );
  OA22X1_RVT U104 ( .A1(n15), .A2(n57), .A3(n58), .A4(n16), .Y(n56) );
  AND2X1_RVT U105 ( .A1(n12), .A2(n11), .Y(n51) );
  OA21X1_RVT U106 ( .A1(n14), .A2(v9), .A3(v0), .Y(n42) );
  NAND2X0_RVT U107 ( .A1(v12), .A2(n51), .Y(n36) );
  AOI21X1_RVT U108 ( .A1(n68), .A2(v2), .A3(v7), .Y(n58) );
  NAND2X0_RVT U109 ( .A1(v8), .A2(n33), .Y(n57) );
  OA22X1_RVT U110 ( .A1(n17), .A2(n59), .A3(n66), .A4(n11), .Y(n55) );
  NAND2X0_RVT U111 ( .A1(v7), .A2(n68), .Y(n59) );
  NAND4X0_RVT U112 ( .A1(n20), .A2(n21), .A3(v4), .A4(n22), .Y(n19) );
  AND3X1_RVT U113 ( .A1(n8), .A2(n67), .A3(n14), .Y(n22) );
  AND2X1_RVT U114 ( .A1(n23), .A2(n24), .Y(Lv13_D_7) );
  OA21X1_RVT U115 ( .A1(n26), .A2(n27), .A3(n62), .Y(n25) );
  AND2X1_RVT U116 ( .A1(n66), .A2(v4), .Y(n27) );
  NAND3X0_RVT U117 ( .A1(n48), .A2(n8), .A3(n20), .Y(n47) );
  OAI21X1_RVT U118 ( .A1(n31), .A2(n11), .A3(n37), .Y(n48) );
  AO21X1_RVT U119 ( .A1(v5), .A2(v0), .A3(n8), .Y(n52) );
  AO21X1_RVT U120 ( .A1(n65), .A2(n40), .A3(n3), .Y(Lv13_D_3) );
  NAND2X0_RVT U121 ( .A1(n42), .A2(n43), .Y(n40) );
  INVX1_RVT U122 ( .A(n41), .Y(n3) );
  NAND3X0_RVT U123 ( .A1(v10), .A2(n17), .A3(v1), .Y(n43) );
  NAND3X0_RVT U124 ( .A1(v0), .A2(n65), .A3(v1), .Y(n45) );
  NAND3X0_RVT U125 ( .A1(v8), .A2(n30), .A3(n23), .Y(n29) );
  OA21X1_RVT U126 ( .A1(n60), .A2(n6), .A3(n23), .Y(Lv13_D_0) );
  INVX1_RVT U127 ( .A(n37), .Y(n6) );
  NAND2X0_RVT U128 ( .A1(n18), .A2(n19), .Y(Lv13_D_9) );
  NOR2X1_RVT U129 ( .A1(v6), .A2(n18), .Y(Lv13_D_8) );
  NAND3X0_RVT U130 ( .A1(n18), .A2(n41), .A3(n47), .Y(Lv13_D_11) );
  NAND4X0_RVT U131 ( .A1(v10), .A2(v0), .A3(n39), .A4(n10), .Y(n18) );
  NAND2X0_RVT U132 ( .A1(n21), .A2(n16), .Y(n37) );
  NAND3X0_RVT U133 ( .A1(n44), .A2(n41), .A3(n45), .Y(Lv13_D_2) );
  NBUFFX2_RVT U134 ( .A(n39), .Y(n64) );
  AND2X1_RVT U135 ( .A1(n35), .A2(n53), .Y(Lv13_D_1) );
  NAND2X0_RVT U136 ( .A1(n31), .A2(n32), .Y(n30) );
  INVX0_RVT U137 ( .A(n31), .Y(n5) );
  NAND2X0_RVT U138 ( .A1(n28), .A2(n29), .Y(Lv13_D_5) );
  AO22X1_RVT U139 ( .A1(v5), .A2(n1), .A3(n25), .A4(n23), .Y(Lv13_D_6) );
  AO22X1_RVT U140 ( .A1(n23), .A2(n34), .A3(n1), .A4(n17), .Y(Lv13_D_4) );
  OR3X2_RVT U141 ( .A1(n33), .A2(n63), .A3(n15), .Y(n32) );
  NAND2X0_RVT U142 ( .A1(v7), .A2(v11), .Y(n31) );
  AND3X1_RVT U143 ( .A1(v1), .A2(n52), .A3(n46), .Y(Lv13_D_10) );
  AND4X1_RVT U144 ( .A1(n46), .A2(v5), .A3(v10), .A4(n13), .Y(Lv13_D_12) );
  NAND3X0_RVT U145 ( .A1(n13), .A2(n17), .A3(n46), .Y(n44) );
  AND2X1_RVT U146 ( .A1(v9), .A2(n64), .Y(n46) );
  INVX0_RVT U147 ( .A(n28), .Y(n1) );
  NBUFFX2_RVT U148 ( .A(n64), .Y(n65) );
  AND3X1_RVT U149 ( .A1(n7), .A2(n4), .A3(n51), .Y(n39) );
  INVX0_RVT U150 ( .A(v11), .Y(n7) );
  INVX0_RVT U151 ( .A(n12), .Y(n66) );
  INVX0_RVT U152 ( .A(n66), .Y(n67) );
  INVX0_RVT U153 ( .A(v7), .Y(n12) );
  NBUFFX2_RVT U154 ( .A(n11), .Y(n68) );
endmodule

