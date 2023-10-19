//
// Milkyway Hierarchical Verilog Dump:
// Generated on 05/16/2023 at 20:38:13
// Design Generated by Consolidated Verilog Reader
// File produced by Consolidated Verilog Writer
// Library Name :s386.mw
// Cell Name    :s386
// Hierarchy delimiter:'/'
// Write Command : write_verilog extracted/outputs/s386_extracted.v
//


module dff_1 (clk , d , q );
input  clk ;
input  d ;
output q ;



DFFX1_RVT q_reg (.D ( d ) , .CLK ( clk ) , .Q ( q ) ) ;
endmodule




module dff_2 (clk , d , q );
input  clk ;
input  d ;
output q ;



DFFX1_RVT q_reg (.D ( d ) , .CLK ( clk ) , .Q ( q ) ) ;
endmodule




module dff_3 (clk , d , q );
input  clk ;
input  d ;
output q ;



DFFX1_RVT q_reg (.D ( d ) , .CLK ( clk ) , .Q ( q ) ) ;
endmodule




module dff_4 (clk , d , q );
input  clk ;
input  d ;
output q ;



DFFX1_RVT q_reg (.D ( d ) , .CLK ( clk ) , .Q ( q ) ) ;
endmodule




module dff_5 (clk , d , q );
input  clk ;
input  d ;
output q ;



DFFX1_RVT q_reg (.D ( d ) , .CLK ( clk ) , .Q ( q ) ) ;
endmodule




module dff_0 (clk , d , q );
input  clk ;
input  d ;
output q ;



DFFX1_RVT q_reg (.D ( d ) , .CLK ( clk ) , .Q ( q ) ) ;
endmodule




module s386 (GND , v5 , v4 , v3 , v2 , v1 , v0 , CK , VDD , 
    v13_D_9 , v13_D_8 , v13_D_7 , v13_D_6 , v13_D_12 , v13_D_11 , 
    v13_D_10 , v6 );
input  GND ;
input  v5 ;
input  v4 ;
input  v3 ;
input  v2 ;
input  v1 ;
input  v0 ;
input  CK ;
input  VDD ;
output v13_D_9 ;
output v13_D_8 ;
output v13_D_7 ;
output v13_D_6 ;
output v13_D_12 ;
output v13_D_11 ;
output v13_D_10 ;
input  v6 ;




dff_1 DFF_5 (.clk ( CK ) , .d ( Lv13_D_0 ) , .q ( v7 ) ) ;


dff_2 DFF_4 (.clk ( CK ) , .d ( Lv13_D_1 ) , .q ( v8 ) ) ;


dff_3 DFF_3 (.clk ( CK ) , .d ( Lv13_D_2 ) , .q ( v9 ) ) ;


dff_4 DFF_2 (.clk ( CK ) , .d ( Lv13_D_3 ) , .q ( v10 ) ) ;


dff_5 DFF_1 (.clk ( CK ) , .d ( Lv13_D_4 ) , .q ( v11 ) ) ;


dff_0 DFF_0 (.clk ( CK ) , .d ( Lv13_D_5 ) , .q ( v12 ) ) ;

INVX0_RVT U94 (.A ( v7 ) , .Y ( n73 ) ) ;
INVX1_RVT U85 (.A ( v8 ) , .Y ( n72 ) ) ;
INVX0_RVT U84 (.A ( v11 ) , .Y ( n71 ) ) ;
NBUFFX2_RVT U74 (.A ( n50 ) , .Y ( n61 ) ) ;
AND2X1_RVT U75 (.Y ( n23 ) , .A1 ( n35 ) , .A2 ( n4 ) ) ;
NAND3X0_RVT U76 (.Y ( n28 ) , .A3 ( n2 ) , .A1 ( v11 ) , .A2 ( n35 ) ) ;
AND2X1_RVT U77 (.Y ( v13_D_7 ) , .A1 ( n23 ) , .A2 ( n24 ) ) ;
AND2X1_RVT U78 (.Y ( Lv13_D_1 ) , .A1 ( n35 ) , .A2 ( n53 ) ) ;
OA21X1_RVT U79 (.Y ( Lv13_D_0 ) , .A3 ( n23 ) , .A2 ( n64 ) , .A1 ( n60 ) ) ;
NAND4X0_RVT U80 (.Y ( n18 ) , .A2 ( v0 ) , .A4 ( n10 ) , .A3 ( n39 ) 
    , .A1 ( v10 ) ) ;
NAND3X0_RVT U81 (.Y ( n45 ) , .A3 ( v1 ) , .A1 ( v0 ) , .A2 ( n67 ) ) ;
INVX1_RVT U82 (.A ( v0 ) , .Y ( n13 ) ) ;
NOR3X0_RVT U83 (.Y ( n35 ) , .A1 ( v10 ) , .A3 ( n50 ) , .A2 ( v9 ) ) ;
INVX1_RVT U86 (.A ( v5 ) , .Y ( n17 ) ) ;
NAND2X0_RVT U87 (.A2 ( n73 ) , .A1 ( v2 ) , .Y ( n33 ) ) ;
INVX1_RVT U88 (.A ( v3 ) , .Y ( n15 ) ) ;
NAND3X0_RVT U89 (.Y ( n34 ) , .A1 ( n37 ) , .A2 ( n73 ) , .A3 ( n38 ) ) ;
NAND3X0_RVT U90 (.Y ( n38 ) , .A1 ( n71 ) , .A2 ( n72 ) , .A3 ( v2 ) ) ;
INVX1_RVT U91 (.A ( v9 ) , .Y ( n10 ) ) ;
INVX1_RVT U92 (.A ( v12 ) , .Y ( n4 ) ) ;
INVX1_RVT U93 (.A ( v1 ) , .Y ( n14 ) ) ;
AND2X1_RVT U95 (.Y ( n20 ) , .A1 ( n4 ) , .A2 ( n10 ) ) ;
INVX1_RVT U96 (.A ( v10 ) , .Y ( n8 ) ) ;
NAND2X0_RVT U97 (.A2 ( n8 ) , .A1 ( n49 ) , .Y ( n41 ) ) ;
AO22X1_RVT U98 (.A2 ( n61 ) , .A3 ( n51 ) , .Y ( n49 ) , .A4 ( n9 ) , .A1 ( n20 ) ) ;
INVX1_RVT U99 (.A ( n42 ) , .Y ( n9 ) ) ;
INVX1_RVT U100 (.A ( n36 ) , .Y ( n2 ) ) ;
OAI22X1_RVT U101 (.Y ( n53 ) , .A4 ( n54 ) , .A3 ( v12 ) , .A2 ( n36 ) 
    , .A1 ( v11 ) ) ;
OA22X1_RVT U102 (.Y ( n54 ) , .A4 ( n56 ) , .A3 ( v11 ) , .A2 ( n71 ) 
    , .A1 ( n55 ) ) ;
OA22X1_RVT U103 (.Y ( n56 ) , .A4 ( n16 ) , .A3 ( n58 ) , .A2 ( n57 ) 
    , .A1 ( n15 ) ) ;
AND2X1_RVT U104 (.Y ( n51 ) , .A1 ( n73 ) , .A2 ( n72 ) ) ;
NAND2X0_RVT U105 (.A2 ( n14 ) , .A1 ( v0 ) , .Y ( n50 ) ) ;
OA21X1_RVT U106 (.Y ( n42 ) , .A3 ( v0 ) , .A2 ( v9 ) , .A1 ( n14 ) ) ;
NAND2X0_RVT U107 (.A2 ( n51 ) , .A1 ( v12 ) , .Y ( n36 ) ) ;
AOI21X1_RVT U108 (.Y ( n58 ) , .A2 ( v2 ) , .A3 ( v7 ) , .A1 ( n72 ) ) ;
NAND2X0_RVT U109 (.A2 ( n33 ) , .A1 ( v8 ) , .Y ( n57 ) ) ;
OA22X1_RVT U110 (.Y ( n55 ) , .A4 ( n72 ) , .A3 ( v7 ) , .A2 ( n59 ) 
    , .A1 ( n17 ) ) ;
NAND2X0_RVT U111 (.A2 ( n72 ) , .A1 ( v7 ) , .Y ( n59 ) ) ;
NAND4X0_RVT U112 (.A2 ( n21 ) , .A4 ( n22 ) , .A3 ( v4 ) , .Y ( n19 ) 
    , .A1 ( n20 ) ) ;
AND3X1_RVT U113 (.A1 ( n8 ) , .Y ( n22 ) , .A2 ( n73 ) , .A3 ( n14 ) ) ;
OA21X1_RVT U114 (.Y ( n25 ) , .A3 ( n71 ) , .A2 ( n27 ) , .A1 ( n26 ) ) ;
AND2X1_RVT U115 (.Y ( n27 ) , .A1 ( v7 ) , .A2 ( v4 ) ) ;
OA22X1_RVT U116 (.Y ( n26 ) , .A4 ( n72 ) , .A3 ( v3 ) , .A2 ( v7 ) , .A1 ( v2 ) ) ;
NAND3X0_RVT U117 (.Y ( n47 ) , .A1 ( n48 ) , .A2 ( n8 ) , .A3 ( n20 ) ) ;
OAI21X1_RVT U118 (.Y ( n48 ) , .A3 ( n37 ) , .A2 ( n72 ) , .A1 ( n31 ) ) ;
AO21X1_RVT U119 (.A1 ( v5 ) , .Y ( n52 ) , .A2 ( v0 ) , .A3 ( n8 ) ) ;
AO21X1_RVT U120 (.A1 ( n67 ) , .Y ( Lv13_D_3 ) , .A2 ( n40 ) , .A3 ( n3 ) ) ;
NAND2X0_RVT U121 (.A2 ( n43 ) , .A1 ( n42 ) , .Y ( n40 ) ) ;
INVX1_RVT U122 (.A ( n41 ) , .Y ( n3 ) ) ;
NAND3X0_RVT U123 (.Y ( n43 ) , .A1 ( v10 ) , .A2 ( n17 ) , .A3 ( v1 ) ) ;
OA21X1_RVT U124 (.Y ( n60 ) , .A3 ( v11 ) , .A2 ( n73 ) , .A1 ( n72 ) ) ;
NAND3X0_RVT U125 (.Y ( n29 ) , .A1 ( v8 ) , .A2 ( n30 ) , .A3 ( n23 ) ) ;
AND2X1_RVT U126 (.Y ( n64 ) , .A1 ( n21 ) , .A2 ( n16 ) ) ;
AND3X1_RVT U127 (.A1 ( n71 ) , .Y ( n21 ) , .A2 ( n15 ) , .A3 ( v8 ) ) ;
INVX1_RVT U128 (.A ( v4 ) , .Y ( n16 ) ) ;
AO21X1_RVT U129 (.A1 ( n5 ) , .Y ( n24 ) , .A2 ( n72 ) , .A3 ( n64 ) ) ;
NAND2X0_RVT U130 (.A2 ( n19 ) , .A1 ( n18 ) , .Y ( v13_D_9 ) ) ;
NOR2X1_RVT U131 (.Y ( v13_D_8 ) , .A2 ( n18 ) , .A1 ( v6 ) ) ;
NAND3X0_RVT U132 (.Y ( v13_D_11 ) , .A1 ( n18 ) , .A2 ( n41 ) , .A3 ( n47 ) ) ;
NAND2X0_RVT U133 (.A2 ( n16 ) , .A1 ( n21 ) , .Y ( n37 ) ) ;
NAND3X0_RVT U134 (.Y ( Lv13_D_2 ) , .A1 ( n44 ) , .A2 ( n41 ) , .A3 ( n45 ) ) ;
NBUFFX2_RVT U135 (.A ( n39 ) , .Y ( n65 ) ) ;
NAND2X0_RVT U136 (.A2 ( n32 ) , .A1 ( n31 ) , .Y ( n30 ) ) ;
INVX0_RVT U137 (.A ( n31 ) , .Y ( n5 ) ) ;
NAND2X0_RVT U138 (.A2 ( n28 ) , .A1 ( n29 ) , .Y ( Lv13_D_5 ) ) ;
AO22X1_RVT U139 (.A2 ( n1 ) , .A3 ( n25 ) , .Y ( v13_D_6 ) , .A4 ( n23 ) 
    , .A1 ( v5 ) ) ;
AO22X1_RVT U140 (.A2 ( n34 ) , .A3 ( n1 ) , .Y ( Lv13_D_4 ) , .A4 ( n17 ) 
    , .A1 ( n23 ) ) ;
OR3X2_RVT U141 (.A1 ( n33 ) , .A3 ( n15 ) , .Y ( n32 ) , .A2 ( v11 ) ) ;
NAND2X0_RVT U142 (.A2 ( v11 ) , .A1 ( v7 ) , .Y ( n31 ) ) ;
AND3X1_RVT U143 (.A1 ( v1 ) , .Y ( v13_D_10 ) , .A2 ( n52 ) , .A3 ( n46 ) ) ;
AND4X1_RVT U144 (.Y ( v13_D_12 ) , .A1 ( n46 ) , .A3 ( v10 ) , .A4 ( n13 ) 
    , .A2 ( v5 ) ) ;
NAND3X0_RVT U145 (.Y ( n44 ) , .A1 ( n13 ) , .A2 ( n17 ) , .A3 ( n46 ) ) ;
AND2X1_RVT U146 (.Y ( n46 ) , .A1 ( v9 ) , .A2 ( n65 ) ) ;
INVX0_RVT U148 (.A ( n28 ) , .Y ( n1 ) ) ;
NBUFFX2_RVT U149 (.A ( n65 ) , .Y ( n67 ) ) ;
AND3X1_RVT U150 (.A1 ( n71 ) , .Y ( n39 ) , .A2 ( n4 ) , .A3 ( n51 ) ) ;
endmodule


