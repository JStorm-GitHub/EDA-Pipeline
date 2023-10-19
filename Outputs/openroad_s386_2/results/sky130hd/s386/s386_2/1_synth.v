/* Generated by Yosys 0.13+15 (git sha1 UNKNOWN, gcc 8.3.1 -fPIC -Os) */

module s386(GND, VDD, CK, v0, v1, v13_D_10, v13_D_11, v13_D_12, v13_D_6, v13_D_7, v13_D_8, v13_D_9, v2, v3, v4, v5, v6);
  wire _000_;
  wire _001_;
  wire _002_;
  wire _003_;
  wire _004_;
  wire _005_;
  wire _006_;
  wire _007_;
  wire _008_;
  wire _009_;
  wire _010_;
  wire _011_;
  wire _012_;
  wire _013_;
  wire _014_;
  wire _015_;
  wire _016_;
  wire _017_;
  wire _018_;
  wire _019_;
  wire _020_;
  wire _021_;
  wire _022_;
  wire _023_;
  wire _024_;
  wire _025_;
  wire _026_;
  wire _027_;
  wire _028_;
  wire _029_;
  wire _030_;
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
  input CK;
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
  sky130_fd_sc_hd__inv_1 _067_ (
    .A(v0),
    .Y(_005_)
  );
  sky130_fd_sc_hd__nor2_2 _068_ (
    .A(\DFF_1.q ),
    .B(\DFF_0.q ),
    .Y(_006_)
  );
  sky130_fd_sc_hd__nor2_4 _069_ (
    .A(\DFF_4.q ),
    .B(\DFF_5.q ),
    .Y(_007_)
  );
  sky130_fd_sc_hd__nand4_1 _070_ (
    .A(_005_),
    .B(\DFF_3.q ),
    .C(_006_),
    .D(_007_),
    .Y(_008_)
  );
  sky130_fd_sc_hd__clkbuf_1 _071_ (
    .A(\DFF_2.q ),
    .X(_009_)
  );
  sky130_fd_sc_hd__nand2_1 _072_ (
    .A(v5),
    .B(_009_),
    .Y(_010_)
  );
  sky130_fd_sc_hd__nor2_1 _073_ (
    .A(_008_),
    .B(_010_),
    .Y(v13_D_12)
  );
  sky130_fd_sc_hd__nor2_1 _074_ (
    .A(\DFF_5.q ),
    .B(\DFF_3.q ),
    .Y(_011_)
  );
  sky130_fd_sc_hd__nand2_1 _075_ (
    .A(_006_),
    .B(_011_),
    .Y(_012_)
  );
  sky130_fd_sc_hd__nand2_1 _076_ (
    .A(v0),
    .B(_009_),
    .Y(_013_)
  );
  sky130_fd_sc_hd__or3_1 _077_ (
    .A(\DFF_4.q ),
    .B(_012_),
    .C(_013_),
    .X(_014_)
  );
  sky130_fd_sc_hd__nor2_1 _078_ (
    .A(v6),
    .B(_014_),
    .Y(v13_D_8)
  );
  sky130_fd_sc_hd__nand2_1 _079_ (
    .A(v0),
    .B(v5),
    .Y(_015_)
  );
  sky130_fd_sc_hd__clkbuf_1 _080_ (
    .A(v1),
    .X(_016_)
  );
  sky130_fd_sc_hd__nand4_1 _081_ (
    .A(\DFF_3.q ),
    .B(_016_),
    .C(_006_),
    .D(_007_),
    .Y(_017_)
  );
  sky130_fd_sc_hd__a21oi_1 _082_ (
    .A1(_009_),
    .A2(_015_),
    .B1(_017_),
    .Y(v13_D_10)
  );
  sky130_fd_sc_hd__buf_2 _083_ (
    .A(\DFF_0.q ),
    .X(_018_)
  );
  sky130_fd_sc_hd__nor2_1 _084_ (
    .A(_009_),
    .B(_016_),
    .Y(_019_)
  );
  sky130_fd_sc_hd__nand3b_1 _085_ (
    .A_N(\DFF_3.q ),
    .B(_019_),
    .C(v0),
    .Y(_020_)
  );
  sky130_fd_sc_hd__nand2b_1 _086_ (
    .A_N(v3),
    .B(\DFF_4.q ),
    .Y(_021_)
  );
  sky130_fd_sc_hd__nor3_2 _087_ (
    .A(\DFF_1.q ),
    .B(v4),
    .C(_021_),
    .Y(_022_)
  );
  sky130_fd_sc_hd__buf_6 _088_ (
    .A(\DFF_4.q ),
    .X(_023_)
  );
  sky130_fd_sc_hd__buf_6 _089_ (
    .A(\DFF_5.q ),
    .X(_024_)
  );
  sky130_fd_sc_hd__nand2_2 _090_ (
    .A(_024_),
    .B(\DFF_1.q ),
    .Y(_025_)
  );
  sky130_fd_sc_hd__nor2_1 _091_ (
    .A(_023_),
    .B(_025_),
    .Y(_026_)
  );
  sky130_fd_sc_hd__nor2_1 _092_ (
    .A(_022_),
    .B(_026_),
    .Y(_027_)
  );
  sky130_fd_sc_hd__nor3_1 _093_ (
    .A(_018_),
    .B(_020_),
    .C(_027_),
    .Y(v13_D_7)
  );
  sky130_fd_sc_hd__nand3_1 _094_ (
    .A(_023_),
    .B(v4),
    .C(_019_),
    .Y(_028_)
  );
  sky130_fd_sc_hd__o22a_1 _095_ (
    .A1(_023_),
    .A2(_013_),
    .B1(_028_),
    .B2(v3),
    .X(_029_)
  );
  sky130_fd_sc_hd__nor2_1 _096_ (
    .A(_012_),
    .B(_029_),
    .Y(v13_D_9)
  );
  sky130_fd_sc_hd__buf_4 _097_ (
    .A(\DFF_1.q ),
    .X(_030_)
  );
  sky130_fd_sc_hd__nand2_1 _098_ (
    .A(_023_),
    .B(_024_),
    .Y(_031_)
  );
  sky130_fd_sc_hd__a21oi_1 _099_ (
    .A1(_030_),
    .A2(_031_),
    .B1(_022_),
    .Y(_032_)
  );
  sky130_fd_sc_hd__nor3_1 _100_ (
    .A(_018_),
    .B(_020_),
    .C(_032_),
    .Y(\DFF_5.d )
  );
  sky130_fd_sc_hd__nand2b_1 _101_ (
    .A_N(\DFF_5.q ),
    .B(v2),
    .Y(_033_)
  );
  sky130_fd_sc_hd__nand2b_1 _102_ (
    .A_N(\DFF_1.q ),
    .B(v3),
    .Y(_034_)
  );
  sky130_fd_sc_hd__o21ai_0 _103_ (
    .A1(_033_),
    .A2(_034_),
    .B1(_025_),
    .Y(_035_)
  );
  sky130_fd_sc_hd__nand3b_1 _104_ (
    .A_N(_018_),
    .B(_035_),
    .C(_023_),
    .Y(_036_)
  );
  sky130_fd_sc_hd__nand3_1 _105_ (
    .A(_030_),
    .B(_018_),
    .C(_007_),
    .Y(_037_)
  );
  sky130_fd_sc_hd__a21oi_1 _106_ (
    .A1(_036_),
    .A2(_037_),
    .B1(_020_),
    .Y(\DFF_0.d )
  );
  sky130_fd_sc_hd__nand2_1 _107_ (
    .A(v2),
    .B(_006_),
    .Y(_038_)
  );
  sky130_fd_sc_hd__nor2_1 _108_ (
    .A(v5),
    .B(_024_),
    .Y(_039_)
  );
  sky130_fd_sc_hd__nand3_1 _109_ (
    .A(_030_),
    .B(\DFF_0.q ),
    .C(_039_),
    .Y(_040_)
  );
  sky130_fd_sc_hd__a21o_1 _110_ (
    .A1(_038_),
    .A2(_040_),
    .B1(_023_),
    .X(_041_)
  );
  sky130_fd_sc_hd__o21bai_1 _111_ (
    .A1(_024_),
    .A2(_022_),
    .B1_N(_018_),
    .Y(_042_)
  );
  sky130_fd_sc_hd__a21oi_1 _112_ (
    .A1(_041_),
    .A2(_042_),
    .B1(_020_),
    .Y(\DFF_1.d )
  );
  sky130_fd_sc_hd__nand4_1 _113_ (
    .A(v5),
    .B(_030_),
    .C(_018_),
    .D(_007_),
    .Y(_043_)
  );
  sky130_fd_sc_hd__and2_2 _114_ (
    .A(_024_),
    .B(v4),
    .X(_044_)
  );
  sky130_fd_sc_hd__o221ai_1 _115_ (
    .A1(_024_),
    .A2(v2),
    .B1(_021_),
    .B2(_044_),
    .C1(_006_),
    .Y(_045_)
  );
  sky130_fd_sc_hd__a21oi_1 _116_ (
    .A1(_043_),
    .A2(_045_),
    .B1(_020_),
    .Y(v13_D_6)
  );
  sky130_fd_sc_hd__nor2_1 _117_ (
    .A(_023_),
    .B(_030_),
    .Y(_046_)
  );
  sky130_fd_sc_hd__nor3b_2 _118_ (
    .A(_025_),
    .B(\DFF_4.q ),
    .C_N(v5),
    .Y(_047_)
  );
  sky130_fd_sc_hd__a31oi_1 _119_ (
    .A1(v4),
    .A2(v2),
    .A3(_046_),
    .B1(_047_),
    .Y(_048_)
  );
  sky130_fd_sc_hd__inv_1 _120_ (
    .A(_030_),
    .Y(_049_)
  );
  sky130_fd_sc_hd__and2b_2 _121_ (
    .A_N(_024_),
    .B(\DFF_0.q ),
    .X(_050_)
  );
  sky130_fd_sc_hd__a31oi_1 _122_ (
    .A1(_024_),
    .A2(_049_),
    .A3(v4),
    .B1(_050_),
    .Y(_051_)
  );
  sky130_fd_sc_hd__a21o_2 _123_ (
    .A1(v3),
    .A2(_033_),
    .B1(_030_),
    .X(_052_)
  );
  sky130_fd_sc_hd__nand3_1 _124_ (
    .A(_023_),
    .B(_025_),
    .C(_052_),
    .Y(_053_)
  );
  sky130_fd_sc_hd__a21boi_0 _125_ (
    .A1(_049_),
    .A2(_007_),
    .B1_N(\DFF_0.q ),
    .Y(_054_)
  );
  sky130_fd_sc_hd__a311oi_1 _126_ (
    .A1(_048_),
    .A2(_051_),
    .A3(_053_),
    .B1(_054_),
    .C1(_020_),
    .Y(\DFF_4.d )
  );
  sky130_fd_sc_hd__inv_1 _127_ (
    .A(_016_),
    .Y(_055_)
  );
  sky130_fd_sc_hd__o21ai_0 _128_ (
    .A1(\DFF_3.q ),
    .A2(_055_),
    .B1(v0),
    .Y(_056_)
  );
  sky130_fd_sc_hd__o21ai_0 _129_ (
    .A1(_030_),
    .A2(_018_),
    .B1(_009_),
    .Y(_057_)
  );
  sky130_fd_sc_hd__nor2_1 _130_ (
    .A(v5),
    .B(_030_),
    .Y(_058_)
  );
  sky130_fd_sc_hd__nand4_1 _131_ (
    .A(_009_),
    .B(_016_),
    .C(_007_),
    .D(_058_),
    .Y(_059_)
  );
  sky130_fd_sc_hd__nor2_1 _132_ (
    .A(\DFF_3.q ),
    .B(_009_),
    .Y(_060_)
  );
  sky130_fd_sc_hd__o21ai_0 _133_ (
    .A1(_005_),
    .A2(_016_),
    .B1(_060_),
    .Y(_061_)
  );
  sky130_fd_sc_hd__a21oi_1 _134_ (
    .A1(_059_),
    .A2(_061_),
    .B1(_018_),
    .Y(_062_)
  );
  sky130_fd_sc_hd__a31o_2 _135_ (
    .A1(_007_),
    .A2(_056_),
    .A3(_057_),
    .B1(_062_),
    .X(\DFF_2.d )
  );
  sky130_fd_sc_hd__a31oi_1 _136_ (
    .A1(v0),
    .A2(_006_),
    .A3(_007_),
    .B1(_060_),
    .Y(_063_)
  );
  sky130_fd_sc_hd__o21ai_0 _137_ (
    .A1(_023_),
    .A2(_024_),
    .B1(_018_),
    .Y(_064_)
  );
  sky130_fd_sc_hd__nand2_1 _138_ (
    .A(_016_),
    .B(_064_),
    .Y(_065_)
  );
  sky130_fd_sc_hd__nor2_1 _139_ (
    .A(\DFF_3.q ),
    .B(_018_),
    .Y(_066_)
  );
  sky130_fd_sc_hd__nor2_1 _140_ (
    .A(v0),
    .B(_009_),
    .Y(_000_)
  );
  sky130_fd_sc_hd__o21ai_0 _141_ (
    .A1(_007_),
    .A2(_066_),
    .B1(_000_),
    .Y(_001_)
  );
  sky130_fd_sc_hd__o221ai_1 _142_ (
    .A1(v5),
    .A2(_008_),
    .B1(_063_),
    .B2(_065_),
    .C1(_001_),
    .Y(\DFF_3.d )
  );
  sky130_fd_sc_hd__a311oi_1 _143_ (
    .A1(_023_),
    .A2(_024_),
    .A3(_030_),
    .B1(_016_),
    .C1(_022_),
    .Y(_002_)
  );
  sky130_fd_sc_hd__nand2_1 _144_ (
    .A(_016_),
    .B(_007_),
    .Y(_003_)
  );
  sky130_fd_sc_hd__a211o_1 _145_ (
    .A1(\DFF_0.q ),
    .A2(_003_),
    .B1(\DFF_3.q ),
    .C1(_009_),
    .X(_004_)
  );
  sky130_fd_sc_hd__o211ai_1 _146_ (
    .A1(_002_),
    .A2(_004_),
    .B1(_014_),
    .C1(_001_),
    .Y(v13_D_11)
  );
  sky130_fd_sc_hd__dfxtp_1 _147_ (
    .CLK(CK),
    .D(\DFF_2.d ),
    .Q(\DFF_2.q )
  );
  sky130_fd_sc_hd__dfxtp_1 _148_ (
    .CLK(CK),
    .D(\DFF_1.d ),
    .Q(\DFF_1.q )
  );
  sky130_fd_sc_hd__dfxtp_1 _149_ (
    .CLK(CK),
    .D(\DFF_0.d ),
    .Q(\DFF_0.q )
  );
  sky130_fd_sc_hd__dfxtp_1 _150_ (
    .CLK(CK),
    .D(\DFF_3.d ),
    .Q(\DFF_3.q )
  );
  sky130_fd_sc_hd__dfxtp_1 _151_ (
    .CLK(CK),
    .D(\DFF_4.d ),
    .Q(\DFF_4.q )
  );
  sky130_fd_sc_hd__dfxtp_1 _152_ (
    .CLK(CK),
    .D(\DFF_5.d ),
    .Q(\DFF_5.q )
  );
endmodule