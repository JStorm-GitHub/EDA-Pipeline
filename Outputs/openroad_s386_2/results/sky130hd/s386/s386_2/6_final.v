module s386 (CK,
    GND,
    VDD,
    v0,
    v1,
    v13_D_10,
    v13_D_11,
    v13_D_12,
    v13_D_6,
    v13_D_7,
    v13_D_8,
    v13_D_9,
    v2,
    v3,
    v4,
    v5,
    v6);
 input CK;
 input GND;
 input VDD;
 input v0;
 input v1;
 output v13_D_10;
 output v13_D_11;
 output v13_D_12;
 output v13_D_6;
 output v13_D_7;
 output v13_D_8;
 output v13_D_9;
 input v2;
 input v3;
 input v4;
 input v5;
 input v6;

 wire \DFF_0.d ;
 wire \DFF_0.q ;
 wire \DFF_1.d ;
 wire \DFF_1.q ;
 wire \DFF_2.d ;
 wire \DFF_2.q ;
 wire \DFF_3.d ;
 wire \DFF_3.q ;
 wire \DFF_4.d ;
 wire \DFF_4.q ;
 wire \DFF_5.d ;
 wire \DFF_5.q ;
 wire _000_;
 wire _001_;
 wire _002_;
 wire _003_;
 wire _004_;
 wire _005_;
 wire _006_;
 wire _007_;
 wire _008_;
 wire net5;
 wire _010_;
 wire _011_;
 wire _012_;
 wire _013_;
 wire _014_;
 wire _015_;
 wire net4;
 wire _017_;
 wire net3;
 wire _019_;
 wire _020_;
 wire _021_;
 wire _022_;
 wire net2;
 wire net1;
 wire _025_;
 wire _026_;
 wire _027_;
 wire _028_;
 wire _029_;
 wire _031_;
 wire _032_;
 wire _033_;
 wire _034_;
 wire _035_;
 wire _036_;
 wire _037_;
 wire _038_;
 wire _039_;
 wire _040_;
 wire _041_;
 wire _042_;
 wire _043_;
 wire _044_;
 wire _045_;
 wire _046_;
 wire _047_;
 wire _048_;
 wire _049_;
 wire _050_;
 wire _051_;
 wire _052_;
 wire _053_;
 wire _054_;
 wire _055_;
 wire _056_;
 wire _057_;
 wire _058_;
 wire _059_;
 wire _060_;
 wire _061_;
 wire _062_;
 wire _063_;
 wire _064_;
 wire _065_;
 wire _066_;
 wire net6;
 wire net7;
 wire net8;
 wire net9;
 wire net10;
 wire net11;
 wire net12;
 wire net13;
 wire net14;
 wire net15;
 wire net16;

 sky130_fd_sc_hd__inv_1 _067_ (.A(net2),
    .Y(_005_));
 sky130_fd_sc_hd__nor2_2 _068_ (.A(\DFF_1.q ),
    .B(\DFF_0.q ),
    .Y(_006_));
 sky130_fd_sc_hd__nor2_4 _069_ (.A(\DFF_4.q ),
    .B(\DFF_5.q ),
    .Y(_007_));
 sky130_fd_sc_hd__nand4_1 _070_ (.A(_005_),
    .B(\DFF_3.q ),
    .C(_006_),
    .D(_007_),
    .Y(_008_));
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_5 ();
 sky130_fd_sc_hd__nand2_1 _072_ (.A(net7),
    .B(\DFF_2.q ),
    .Y(_010_));
 sky130_fd_sc_hd__nor2_1 _073_ (.A(_008_),
    .B(_010_),
    .Y(net11));
 sky130_fd_sc_hd__nor2_1 _074_ (.A(\DFF_5.q ),
    .B(\DFF_3.q ),
    .Y(_011_));
 sky130_fd_sc_hd__nand2_1 _075_ (.A(_006_),
    .B(_011_),
    .Y(_012_));
 sky130_fd_sc_hd__nand2_1 _076_ (.A(net2),
    .B(\DFF_2.q ),
    .Y(_013_));
 sky130_fd_sc_hd__or3_4 _077_ (.A(\DFF_4.q ),
    .B(_012_),
    .C(_013_),
    .X(_014_));
 sky130_fd_sc_hd__nor2_1 _078_ (.A(net8),
    .B(_014_),
    .Y(net14));
 sky130_fd_sc_hd__nand2_1 _079_ (.A(net2),
    .B(net7),
    .Y(_015_));
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_4 ();
 sky130_fd_sc_hd__nand4_1 _081_ (.A(\DFF_3.q ),
    .B(net3),
    .C(_006_),
    .D(_007_),
    .Y(_017_));
 sky130_fd_sc_hd__a21oi_1 _082_ (.A1(\DFF_2.q ),
    .A2(_015_),
    .B1(_017_),
    .Y(net9));
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_3 ();
 sky130_fd_sc_hd__nor2_2 _084_ (.A(\DFF_2.q ),
    .B(net3),
    .Y(_019_));
 sky130_fd_sc_hd__nand3b_2 _085_ (.A_N(\DFF_3.q ),
    .B(_019_),
    .C(net2),
    .Y(_020_));
 sky130_fd_sc_hd__nand2b_4 _086_ (.A_N(\DFF_4.q ),
    .B(net5),
    .Y(_021_));
 sky130_fd_sc_hd__nor3_4 _087_ (.A(\DFF_1.q ),
    .B(net6),
    .C(_021_),
    .Y(_022_));
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_2 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_1 ();
 sky130_fd_sc_hd__nand2_1 _090_ (.A(\DFF_5.q ),
    .B(\DFF_1.q ),
    .Y(_025_));
 sky130_fd_sc_hd__nor2_1 _091_ (.A(\DFF_4.q ),
    .B(_025_),
    .Y(_026_));
 sky130_fd_sc_hd__nor2_1 _092_ (.A(_022_),
    .B(_026_),
    .Y(_027_));
 sky130_fd_sc_hd__nor3_1 _093_ (.A(\DFF_0.q ),
    .B(_020_),
    .C(_027_),
    .Y(net13));
 sky130_fd_sc_hd__nand3_1 _094_ (.A(\DFF_4.q ),
    .B(net6),
    .C(_019_),
    .Y(_028_));
 sky130_fd_sc_hd__o22a_1 _095_ (.A1(\DFF_4.q ),
    .A2(_013_),
    .B1(_028_),
    .B2(net5),
    .X(_029_));
 sky130_fd_sc_hd__nor2_1 _096_ (.A(_012_),
    .B(_029_),
    .Y(net15));
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_0 ();
 sky130_fd_sc_hd__nand2_1 _098_ (.A(\DFF_4.q ),
    .B(\DFF_5.q ),
    .Y(_031_));
 sky130_fd_sc_hd__a21oi_1 _099_ (.A1(\DFF_1.q ),
    .A2(_031_),
    .B1(_022_),
    .Y(_032_));
 sky130_fd_sc_hd__nor3_1 _100_ (.A(\DFF_0.q ),
    .B(_020_),
    .C(_032_),
    .Y(\DFF_5.d ));
 sky130_fd_sc_hd__nand2b_1 _101_ (.A_N(\DFF_5.q ),
    .B(net4),
    .Y(_033_));
 sky130_fd_sc_hd__nand2b_1 _102_ (.A_N(\DFF_1.q ),
    .B(net5),
    .Y(_034_));
 sky130_fd_sc_hd__o21ai_0 _103_ (.A1(_033_),
    .A2(_034_),
    .B1(_025_),
    .Y(_035_));
 sky130_fd_sc_hd__nand3b_1 _104_ (.A_N(\DFF_0.q ),
    .B(_035_),
    .C(\DFF_4.q ),
    .Y(_036_));
 sky130_fd_sc_hd__nand3_1 _105_ (.A(\DFF_1.q ),
    .B(\DFF_0.q ),
    .C(_007_),
    .Y(_037_));
 sky130_fd_sc_hd__a21oi_1 _106_ (.A1(_036_),
    .A2(_037_),
    .B1(_020_),
    .Y(\DFF_0.d ));
 sky130_fd_sc_hd__nand2_1 _107_ (.A(net4),
    .B(_006_),
    .Y(_038_));
 sky130_fd_sc_hd__nor2_1 _108_ (.A(net7),
    .B(\DFF_5.q ),
    .Y(_039_));
 sky130_fd_sc_hd__nand3_1 _109_ (.A(\DFF_1.q ),
    .B(\DFF_0.q ),
    .C(_039_),
    .Y(_040_));
 sky130_fd_sc_hd__a21o_1 _110_ (.A1(_038_),
    .A2(_040_),
    .B1(\DFF_4.q ),
    .X(_041_));
 sky130_fd_sc_hd__o21bai_1 _111_ (.A1(\DFF_5.q ),
    .A2(_022_),
    .B1_N(\DFF_0.q ),
    .Y(_042_));
 sky130_fd_sc_hd__a21oi_1 _112_ (.A1(_041_),
    .A2(_042_),
    .B1(_020_),
    .Y(\DFF_1.d ));
 sky130_fd_sc_hd__nand4_1 _113_ (.A(net7),
    .B(\DFF_1.q ),
    .C(\DFF_0.q ),
    .D(_007_),
    .Y(_043_));
 sky130_fd_sc_hd__and2_0 _114_ (.A(\DFF_5.q ),
    .B(net6),
    .X(_044_));
 sky130_fd_sc_hd__o221ai_1 _115_ (.A1(\DFF_5.q ),
    .A2(net4),
    .B1(net16),
    .B2(_044_),
    .C1(_006_),
    .Y(_045_));
 sky130_fd_sc_hd__a21oi_1 _116_ (.A1(_043_),
    .A2(_045_),
    .B1(_020_),
    .Y(net12));
 sky130_fd_sc_hd__nor2_1 _117_ (.A(\DFF_4.q ),
    .B(\DFF_1.q ),
    .Y(_046_));
 sky130_fd_sc_hd__nor3b_1 _118_ (.A(_025_),
    .B(\DFF_4.q ),
    .C_N(net7),
    .Y(_047_));
 sky130_fd_sc_hd__a31oi_1 _119_ (.A1(net6),
    .A2(net4),
    .A3(_046_),
    .B1(_047_),
    .Y(_048_));
 sky130_fd_sc_hd__inv_1 _120_ (.A(\DFF_1.q ),
    .Y(_049_));
 sky130_fd_sc_hd__and2b_1 _121_ (.A_N(\DFF_5.q ),
    .B(\DFF_0.q ),
    .X(_050_));
 sky130_fd_sc_hd__a31oi_1 _122_ (.A1(\DFF_5.q ),
    .A2(_049_),
    .A3(net6),
    .B1(_050_),
    .Y(_051_));
 sky130_fd_sc_hd__a21o_1 _123_ (.A1(net5),
    .A2(_033_),
    .B1(\DFF_1.q ),
    .X(_052_));
 sky130_fd_sc_hd__nand3_1 _124_ (.A(\DFF_4.q ),
    .B(_025_),
    .C(_052_),
    .Y(_053_));
 sky130_fd_sc_hd__a21boi_0 _125_ (.A1(_049_),
    .A2(_007_),
    .B1_N(\DFF_0.q ),
    .Y(_054_));
 sky130_fd_sc_hd__a311oi_1 _126_ (.A1(_048_),
    .A2(_051_),
    .A3(_053_),
    .B1(_054_),
    .C1(_020_),
    .Y(\DFF_4.d ));
 sky130_fd_sc_hd__inv_1 _127_ (.A(net3),
    .Y(_055_));
 sky130_fd_sc_hd__o21ai_0 _128_ (.A1(\DFF_3.q ),
    .A2(_055_),
    .B1(net2),
    .Y(_056_));
 sky130_fd_sc_hd__o21ai_0 _129_ (.A1(\DFF_1.q ),
    .A2(\DFF_0.q ),
    .B1(\DFF_2.q ),
    .Y(_057_));
 sky130_fd_sc_hd__nor2_1 _130_ (.A(net7),
    .B(\DFF_1.q ),
    .Y(_058_));
 sky130_fd_sc_hd__nand4_1 _131_ (.A(\DFF_2.q ),
    .B(net3),
    .C(_007_),
    .D(_058_),
    .Y(_059_));
 sky130_fd_sc_hd__nor2_1 _132_ (.A(\DFF_3.q ),
    .B(\DFF_2.q ),
    .Y(_060_));
 sky130_fd_sc_hd__o21ai_0 _133_ (.A1(_005_),
    .A2(net3),
    .B1(_060_),
    .Y(_061_));
 sky130_fd_sc_hd__a21oi_1 _134_ (.A1(_059_),
    .A2(_061_),
    .B1(\DFF_0.q ),
    .Y(_062_));
 sky130_fd_sc_hd__a31o_1 _135_ (.A1(_007_),
    .A2(_056_),
    .A3(_057_),
    .B1(_062_),
    .X(\DFF_2.d ));
 sky130_fd_sc_hd__a31oi_1 _136_ (.A1(net2),
    .A2(_006_),
    .A3(_007_),
    .B1(_060_),
    .Y(_063_));
 sky130_fd_sc_hd__o21ai_0 _137_ (.A1(\DFF_4.q ),
    .A2(\DFF_5.q ),
    .B1(\DFF_0.q ),
    .Y(_064_));
 sky130_fd_sc_hd__nand2_1 _138_ (.A(net3),
    .B(_064_),
    .Y(_065_));
 sky130_fd_sc_hd__nor2_1 _139_ (.A(\DFF_3.q ),
    .B(\DFF_0.q ),
    .Y(_066_));
 sky130_fd_sc_hd__nor2_1 _140_ (.A(net2),
    .B(\DFF_2.q ),
    .Y(_000_));
 sky130_fd_sc_hd__o21ai_0 _141_ (.A1(_007_),
    .A2(_066_),
    .B1(_000_),
    .Y(_001_));
 sky130_fd_sc_hd__o221ai_1 _142_ (.A1(net7),
    .A2(_008_),
    .B1(_063_),
    .B2(_065_),
    .C1(_001_),
    .Y(\DFF_3.d ));
 sky130_fd_sc_hd__a311oi_2 _143_ (.A1(\DFF_4.q ),
    .A2(\DFF_5.q ),
    .A3(\DFF_1.q ),
    .B1(net3),
    .C1(_022_),
    .Y(_002_));
 sky130_fd_sc_hd__nand2_1 _144_ (.A(net3),
    .B(_007_),
    .Y(_003_));
 sky130_fd_sc_hd__a211o_1 _145_ (.A1(\DFF_0.q ),
    .A2(_003_),
    .B1(\DFF_3.q ),
    .C1(\DFF_2.q ),
    .X(_004_));
 sky130_fd_sc_hd__o211ai_2 _146_ (.A1(_002_),
    .A2(_004_),
    .B1(_014_),
    .C1(_001_),
    .Y(net10));
 sky130_fd_sc_hd__dfxtp_2 _147_ (.D(\DFF_2.d ),
    .Q(\DFF_2.q ),
    .CLK(net1));
 sky130_fd_sc_hd__dfxtp_4 _148_ (.D(\DFF_1.d ),
    .Q(\DFF_1.q ),
    .CLK(net1));
 sky130_fd_sc_hd__dfxtp_4 _149_ (.D(\DFF_0.d ),
    .Q(\DFF_0.q ),
    .CLK(net1));
 sky130_fd_sc_hd__dfxtp_2 _150_ (.D(\DFF_3.d ),
    .Q(\DFF_3.q ),
    .CLK(net1));
 sky130_fd_sc_hd__dfxtp_4 _151_ (.D(\DFF_4.d ),
    .Q(\DFF_4.q ),
    .CLK(net1));
 sky130_fd_sc_hd__dfxtp_4 _152_ (.D(\DFF_5.d ),
    .Q(\DFF_5.q ),
    .CLK(net1));
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_6 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_7 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_8 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_9 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_10 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_11 ();
 sky130_fd_sc_hd__tapvpwrvgnd_1 TAP_12 ();
 sky130_fd_sc_hd__dlymetal6s2s_1 input1 (.A(CK),
    .X(net1));
 sky130_fd_sc_hd__buf_6 input2 (.A(v0),
    .X(net2));
 sky130_fd_sc_hd__buf_8 input3 (.A(v1),
    .X(net3));
 sky130_fd_sc_hd__dlymetal6s2s_1 input4 (.A(v2),
    .X(net4));
 sky130_fd_sc_hd__buf_6 input5 (.A(v3),
    .X(net5));
 sky130_fd_sc_hd__buf_8 input6 (.A(v4),
    .X(net6));
 sky130_fd_sc_hd__clkbuf_2 input7 (.A(v5),
    .X(net7));
 sky130_fd_sc_hd__clkbuf_1 input8 (.A(v6),
    .X(net8));
 sky130_fd_sc_hd__clkbuf_1 output9 (.A(net9),
    .X(v13_D_10));
 sky130_fd_sc_hd__clkbuf_1 output10 (.A(net10),
    .X(v13_D_11));
 sky130_fd_sc_hd__clkbuf_1 output11 (.A(net11),
    .X(v13_D_12));
 sky130_fd_sc_hd__clkbuf_1 output12 (.A(net12),
    .X(v13_D_6));
 sky130_fd_sc_hd__clkbuf_1 output13 (.A(net13),
    .X(v13_D_7));
 sky130_fd_sc_hd__clkbuf_1 output14 (.A(net14),
    .X(v13_D_8));
 sky130_fd_sc_hd__clkbuf_1 output15 (.A(net15),
    .X(v13_D_9));
 sky130_fd_sc_hd__dlymetal6s2s_1 rebuffer1 (.A(_021_),
    .X(net16));
 sky130_fd_sc_hd__fill_4 FILLER_0_0_0 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_0_52 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_2_0 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_2_28 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_2_42 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_2_51 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_2_57 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_3_10 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_3_31 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_3_65 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_4_10 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_4_28 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_4_31 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_4_35 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_4_39 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_4_47 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_5_18 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_5_22 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_5_37 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_5_41 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_5_43 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_5_47 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_5_66 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_6_0 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_6_4 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_6_6 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_6_22 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_6_29 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_6_31 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_6_33 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_6_38 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_6_49 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_6_65 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_7_0 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_7_4 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_7_6 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_7_13 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_7_18 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_7_22 ();
 sky130_fd_sc_hd__fill_8 FILLER_0_7_27 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_7_35 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_7_45 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_7_61 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_7_65 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_8_0 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_8_4 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_8_31 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_8_37 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_8_41 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_8_47 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_8_49 ();
 sky130_fd_sc_hd__fill_8 FILLER_0_9_0 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_9_8 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_9_12 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_9_17 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_9_19 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_9_39 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_9_61 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_9_65 ();
 sky130_fd_sc_hd__fill_8 FILLER_0_10_0 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_10_8 ();
 sky130_fd_sc_hd__fill_1 FILLER_0_10_10 ();
 sky130_fd_sc_hd__fill_4 FILLER_0_10_61 ();
 sky130_fd_sc_hd__fill_2 FILLER_0_10_65 ();
endmodule
