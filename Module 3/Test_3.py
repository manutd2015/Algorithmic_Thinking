"""
Algorithmic Thinking - Module 3
10-5-2014

Divide and Conquer Method and Clustering
Closest Pairs and Clustering Algorithms
Test File
"""

import alg_cluster
import Project_3 as prj3

slow_dist = True
fast_dist = True


if slow_dist == True:
    print "-------Testing Slow closest pairs first-------"
    print "\nTest 1.."
    print prj3.slow_closest_pairs([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0)])
    print "Expected: set([(1.0, 0, 1)])"
    print "\nTest 2.."
    print prj3.slow_closest_pairs([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 0, 1, 1, 0), alg_cluster.Cluster(set([]), 0, 2, 1, 0)])
    print "Expected: set([(1.0, 0, 1), (1.0, 1, 2)])" 
    
if fast_dist == True:
    print "\n" + "-------Testing fast closest pairs-------"
    print "\nTest 1..."
    print prj3.fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0)])
    print "\nTest 2..."
    print prj3.fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), alg_cluster.Cluster(set([]), 1, 0, 1, 0), alg_cluster.Cluster(set([]), 2, 0, 1, 0), alg_cluster.Cluster(set([]), 3, 0, 1, 0), alg_cluster.Cluster(set([]), 4, 0, 1, 0), alg_cluster.Cluster(set([]), 5, 0, 1, 0), alg_cluster.Cluster(set([]), 6, 0, 1, 0), alg_cluster.Cluster(set([]), 7, 0, 1, 0), alg_cluster.Cluster(set([]), 8, 0, 1, 0), alg_cluster.Cluster(set([]), 9, 0, 1, 0), alg_cluster.Cluster(set([]), 10, 0, 1, 0), alg_cluster.Cluster(set([]), 11, 0, 1, 0), alg_cluster.Cluster(set([]), 12, 0, 1, 0), alg_cluster.Cluster(set([]), 13, 0, 1, 0), alg_cluster.Cluster(set([]), 14, 0, 1, 0), alg_cluster.Cluster(set([]), 15, 0, 1, 0), alg_cluster.Cluster(set([]), 16, 0, 1, 0), alg_cluster.Cluster(set([]), 17, 0, 1, 0), alg_cluster.Cluster(set([]), 18, 0, 1, 0), alg_cluster.Cluster(set([]), 19, 0, 1, 0)])
    print "Expected: one of the tuples in set([(1.0, 9, 10), (1.0, 2, 3), (1.0, 15, 16), (1.0, 11, 12), (1.0, 13, 14), (1.0, 16, 17), (1.0, 14, 15), (1.0, 12, 13), (1.0, 4, 5), (1.0, 18, 19), (1.0, 3, 4), (1.0, 8, 9), (1.0, 17, 18), (1.0, 6, 7), (1.0, 7, 8), (1.0, 5, 6), (1.0, 10, 11), (1.0, 0, 1), (1.0, 1, 2)])"
    print "\nTest 3..."
    print prj3.fast_closest_pair([alg_cluster.Cluster(set([]), 90.9548590217, -17.089022585, 1, 0), alg_cluster.Cluster(set([]), 90.2536656675, -70.5911544718, 1, 0), alg_cluster.Cluster(set([]), -57.5872347006, 99.7124028905, 1, 0), alg_cluster.Cluster(set([]), -15.9338519877, 5.91547495626, 1, 0), alg_cluster.Cluster(set([]), 19.1869055492, -28.0681513017, 1, 0), alg_cluster.Cluster(set([]), -23.0752410653, -42.1353490324, 1, 0), alg_cluster.Cluster(set([]), -65.1732261872, 19.675582646, 1, 0), alg_cluster.Cluster(set([]), 99.7789872101, -11.2619165604, 1, 0), alg_cluster.Cluster(set([]), -43.3699854405, -94.7349852817, 1, 0), alg_cluster.Cluster(set([]), 48.2281912402, -53.3441788034, 1, 0)])
    print "Expected: one of the tuples in set([(10.5745166749, 0, 7)])"
    print "\nTest 4..."
    print prj3.fast_closest_pair([alg_cluster.Cluster(set(['01101']), 720.281573781, 440.436162917, 223510, 5.7e-05), alg_cluster.Cluster(set(['01121']), 718.485365885, 413.521338651, 80321, 4.9e-05), alg_cluster.Cluster(set(['01117']), 709.193528999, 417.394467797, 143293, 5.6e-05), alg_cluster.Cluster(set(['01125']), 692.900099393, 417.773844647, 164875, 5.4e-05), alg_cluster.Cluster(set(['01073']), 704.191210749, 411.014665198, 662047, 7.3e-05), alg_cluster.Cluster(set(['01115']), 714.563978269, 406.272136377, 64742, 4.7e-05), alg_cluster.Cluster(set(['01015']), 723.907941153, 403.837487318, 112249, 5.6e-05), alg_cluster.Cluster(set(['01055']), 719.112287909, 398.290991634, 103459, 4.9e-05), alg_cluster.Cluster(set(['01103']), 702.624988295, 389.788894045, 111064, 5.3e-05), alg_cluster.Cluster(set(['01033', '01077']), 685.447113541, 382.760589081, 142950, 4.6e-05), alg_cluster.Cluster(set(['01089']), 707.938558006, 382.483904975, 276700, 5.1e-05), alg_cluster.Cluster(set(['01081']), 736.280761314, 430.281309969, 115092, 5e-05), alg_cluster.Cluster(set(['01113']), 740.385154867, 436.939588695, 49756, 5.6e-05), alg_cluster.Cluster(set(['05119']), 598.676543754, 389.524749021, 361474, 5.3e-05), alg_cluster.Cluster(set(['05139']), 595.14987863, 427.226433206, 45629, 5.4e-05), alg_cluster.Cluster(set(['04013']), 214.128077618, 396.893960776, 3072149, 6.8e-05), alg_cluster.Cluster(set(['06025']), 156.397958859, 393.161127277, 142361, 5.6e-05), alg_cluster.Cluster(set(['06065']), 146.410389633, 374.21707964, 1545387, 6.1e-05), alg_cluster.Cluster(set(['06073']), 129.2075529, 387.064888184, 2813833, 6.6e-05), alg_cluster.Cluster(set(['06059']), 113.997715586, 368.503452566, 2846289, 9.8e-05), alg_cluster.Cluster(set(['06037']), 105.369854549, 359.050126004, 9519338, 0.00011), alg_cluster.Cluster(set(['06111']), 93.4973310868, 344.590570899, 753197, 5.8e-05), alg_cluster.Cluster(set(['06083']), 76.0382837186, 340.420376302, 399347, 6.4e-05), alg_cluster.Cluster(set(['06029']), 103.787886113, 326.006585349, 661645, 9.7e-05), alg_cluster.Cluster(set(['06071']), 148.402461892, 350.061039619, 1709434, 7.7e-05), alg_cluster.Cluster(set(['06027']), 136.048381588, 306.102582286, 17945, 5.3e-05), alg_cluster.Cluster(set(['06107']), 108.085024898, 306.351832438, 368021, 5.8e-05), alg_cluster.Cluster(set(['06031']), 89.2713893096, 304.772281089, 129461, 5.1e-05), alg_cluster.Cluster(set(['06039']), 97.2145136451, 278.975077449, 123109, 6e-05), alg_cluster.Cluster(set(['06019']), 95.6093812211, 290.162708843, 799407, 6.4e-05), alg_cluster.Cluster(set(['06047']), 80.1217093401, 275.749681794, 210554, 4.7e-05), alg_cluster.Cluster(set(['06081']), 52.6171444847, 262.707477827, 707161, 5.6e-05), alg_cluster.Cluster(set(['06001']), 61.782098866, 259.312457296, 1443741, 7e-05), alg_cluster.Cluster(set(['06085']), 63.1509653633, 270.516712105, 1682585, 6.3e-05), alg_cluster.Cluster(set(['06099']), 77.5948233373, 265.302047042, 446997, 5.1e-05), alg_cluster.Cluster(set(['06077']), 74.1740312349, 256.485831492, 563598, 5.2e-05), alg_cluster.Cluster(set(['06013']), 62.7064814493, 253.075658488, 948816, 5e-05), alg_cluster.Cluster(set(['06067']), 74.3547338322, 245.49501455, 1223499, 6.1e-05), alg_cluster.Cluster(set(['06095']), 64.1452346104, 245.330036641, 394542, 4.6e-05), alg_cluster.Cluster(set(['06075']), 52.7404001225, 254.517429395, 776733, 8.4e-05), alg_cluster.Cluster(set(['06113']), 68.2602083189, 236.862609218, 168660, 5.9e-05), alg_cluster.Cluster(set(['06061']), 90.0298511972, 233.575536165, 248399, 5.2e-05), alg_cluster.Cluster(set(['06115']), 81.8982358215, 225.444950413, 60219, 4.9e-05), alg_cluster.Cluster(set(['06101']), 74.2003718491, 229.646592975, 78930, 5.6e-05), alg_cluster.Cluster(set(['06007']), 79.7767444918, 214.910128237, 203171, 4.7e-05), alg_cluster.Cluster(set(['06021']), 65.2043358182, 213.245337355, 26453, 6.9e-05), alg_cluster.Cluster(set(['06089']), 77.359494209, 188.945068958, 163256, 5.7e-05), alg_cluster.Cluster(set(['08005', '08001']), 380.140193285, 268.051898162, 851824, 6.19900531096e-05), alg_cluster.Cluster(set(['08031']), 371.038986573, 266.847932979, 554636, 7.9e-05), alg_cluster.Cluster(set(['08059']), 364.301409054, 270.903209636, 527056, 5.5e-05), alg_cluster.Cluster(set(['09003']), 925.917212741, 177.152290276, 857183, 5.7e-05), alg_cluster.Cluster(set(['09005']), 917.693447363, 179.72354771, 182193, 4.8e-05), alg_cluster.Cluster(set(['09001']), 917.147792831, 191.892113077, 882567, 5.3e-05), alg_cluster.Cluster(set(['09009']), 924.915452791, 187.557375239, 824008, 5.4e-05), alg_cluster.Cluster(set(['09007']), 931.146412937, 184.643328414, 155071, 5.1e-05), alg_cluster.Cluster(set(['09013']), 932.609837236, 174.394154191, 136364, 5e-05), alg_cluster.Cluster(set(['10003']), 888.26796027, 239.785084878, 500265, 4.9e-05), alg_cluster.Cluster(set(['12071']), 822.736368501, 559.319167615, 440888, 4.7e-05), alg_cluster.Cluster(set(['12086']), 855.717845944, 576.450702277, 2253362, 4.9e-05), alg_cluster.Cluster(set(['12011']), 854.318125011, 564.174521982, 1623018, 5e-05), alg_cluster.Cluster(set(['12099']), 852.886370359, 552.951546188, 1131184, 5.1e-05), alg_cluster.Cluster(set(['12057']), 810.083518173, 529.957501469, 998948, 4.7e-05), alg_cluster.Cluster(set(['12095', '12117']), 828.826823208, 511.667716297, 1261540, 5.11315471566e-05), alg_cluster.Cluster(set(['12019']), 812.760924762, 481.531359294, 140814, 4.6e-05), alg_cluster.Cluster(set(['12073']), 762.463896365, 477.365342219, 239452, 6.1e-05), alg_cluster.Cluster(set(['12065']), 770.707334208, 476.851119419, 12902, 4.7e-05), alg_cluster.Cluster(set(['12023']), 796.544243535, 477.588016437, 56513, 5e-05), alg_cluster.Cluster(set(['12031']), 815.145119735, 473.114295395, 778879, 4.9e-05), alg_cluster.Cluster(set(['13087']), 755.693541123, 468.194002931, 28240, 4.9e-05), alg_cluster.Cluster(set(['13275']), 768.884153625, 466.608446685, 42737, 5.5e-05), alg_cluster.Cluster(set(['13095']), 761.086378978, 451.967184234, 96065, 4.9e-05), alg_cluster.Cluster(set(['13115']), 734.580792996, 390.450110664, 90565, 5.2e-05), alg_cluster.Cluster(set(['13313', '13047', '13295']), 734.792678283, 378.16072481, 197860, 5.37671181644e-05), alg_cluster.Cluster(set(['13215']), 745.265661102, 430.987078939, 186291, 5.9e-05), alg_cluster.Cluster(set(['13285']), 741.206792819, 419.291408746, 58779, 4.7e-05), alg_cluster.Cluster(set(['13045']), 738.792024777, 406.300529008, 87268, 4.6e-05), alg_cluster.Cluster(set(['13097', '13223']), 743.272561563, 400.714055725, 173852, 5.06509329775e-05), alg_cluster.Cluster(set(['13129']), 740.472181415, 384.60635928, 44104, 5e-05), alg_cluster.Cluster(set(['13015']), 741.560012096, 390.864452051, 76019, 4.8e-05), alg_cluster.Cluster(set(['13067', '13089', '13121']), 750.682394625, 399.195844304, 2089622, 6.76176380226e-05), alg_cluster.Cluster(set(['13077']), 745.613117606, 411.392480996, 89215, 4.7e-05), alg_cluster.Cluster(set(['13153']), 768.866056624, 429.26170891, 110765, 4.6e-05), alg_cluster.Cluster(set(['13021']), 767.744846588, 421.175433164, 153887, 5.4e-05), alg_cluster.Cluster(set(['13113', '13255', '13063', '13151']), 753.455694533, 407.976008734, 505538, 5.89670094038e-05), alg_cluster.Cluster(set(['13057']), 748.412720226, 389.846908157, 141903, 5.3e-05), alg_cluster.Cluster(set(['13117']), 755.145102581, 389.478397813, 98407, 5.1e-05), alg_cluster.Cluster(set(['13135']), 758.038826857, 395.110327675, 588448, 6.3e-05), alg_cluster.Cluster(set(['13247', '13217']), 760.136606655, 403.38199347, 132112, 5.41227746155e-05), alg_cluster.Cluster(set(['13013', '13297']), 763.824955527, 396.644405603, 106831, 4.87041963475e-05), alg_cluster.Cluster(set(['13219', '13059']), 770.124456082, 394.603787436, 127714, 5.17679502639e-05), alg_cluster.Cluster(set(['13073', '13245']), 795.565595936, 403.239414826, 289063, 5.62200108627e-05), alg_cluster.Cluster(set(['19163', '17161']), 622.251364027, 229.337743865, 308042, 5.30905136313e-05), alg_cluster.Cluster(set(['19153']), 570.801738263, 228.668095362, 374601, 5.2e-05), alg_cluster.Cluster(set(['19013']), 591.836020306, 209.588448378, 128012, 4.6e-05), alg_cluster.Cluster(set(['19057']), 612.882010424, 244.949915243, 42351, 5.1e-05), alg_cluster.Cluster(set(['17031', '17043']), 668.403256539, 219.438581907, 6280902, 5.95604599467e-05), alg_cluster.Cluster(set(['17201']), 645.722085, 209.852492823, 278418, 4.8e-05), alg_cluster.Cluster(set(['18089']), 677.840033419, 228.268571284, 484564, 4.8e-05), alg_cluster.Cluster(set(['18097']), 703.47637833, 264.614798668, 860454, 4.8e-05), alg_cluster.Cluster(set(['20173']), 502.059178492, 322.563937328, 452869, 5.1e-05), alg_cluster.Cluster(set(['20091', '20209']), 550.128980432, 293.196943167, 608968, 5.02592615704e-05), alg_cluster.Cluster(set(['21019']), 768.726553092, 290.270551648, 49752, 5.8e-05), alg_cluster.Cluster(set(['21067']), 738.000675961, 302.005037855, 260512, 4.8e-05), alg_cluster.Cluster(set(['21117', '39061']), 733.385791369, 276.204710617, 996767, 5.33921789144e-05), alg_cluster.Cluster(set(['21111']), 715.347723878, 301.167740487, 693604, 5.9e-05), alg_cluster.Cluster(set(['22017', '22015']), 572.234109108, 441.521371486, 350471, 5.83533930054e-05), alg_cluster.Cluster(set(['22047', '22121']), 622.291274579, 491.551667262, 54921, 4.89665519564e-05), alg_cluster.Cluster(set(['22033']), 627.532921181, 486.959525017, 412852, 5.3e-05), alg_cluster.Cluster(set(['22095']), 639.022908787, 496.564276607, 43044, 5.1e-05), alg_cluster.Cluster(set(['22071']), 651.338581076, 496.465402252, 484674, 6.4e-05), alg_cluster.Cluster(set(['22051']), 647.254240096, 504.485538044, 455466, 4.6e-05), alg_cluster.Cluster(set(['25017']), 943.405755498, 156.504310828, 1465396, 5.6e-05), alg_cluster.Cluster(set(['25025', '25021']), 949.577214992, 160.35336448, 1340115, 6.17505318573e-05), alg_cluster.Cluster(set(['25013', '25015']), 925.242035827, 168.221353927, 608479, 5.04987057894e-05), alg_cluster.Cluster(set(['24001']), 834.528507681, 249.862506444, 74930, 4.8e-05), alg_cluster.Cluster(set(['24043']), 849.08430905, 247.089766046, 131923, 4.6e-05), alg_cluster.Cluster(set(['24510', '24005']), 872.39640107, 248.277002427, 1405446, 6.70230005279e-05), alg_cluster.Cluster(set(['24003']), 874.299504257, 257.092978322, 489656, 5.3e-05), alg_cluster.Cluster(set(['24027', '24031']), 864.052831424, 254.879514396, 1121183, 6.38947299415e-05), alg_cluster.Cluster(set(['24025']), 876.595690503, 242.900377968, 218590, 4.6e-05), alg_cluster.Cluster(set(['24021']), 858.130790832, 248.37974611, 195277, 5e-05), alg_cluster.Cluster(set(['26163']), 746.37046732, 200.570021537, 2061162, 6.4e-05), alg_cluster.Cluster(set(['26125']), 743.036942153, 192.129690868, 1194156, 5.7e-05), alg_cluster.Cluster(set(['26099']), 750.610280372, 190.468671453, 788149, 5.1e-05), alg_cluster.Cluster(set(['27123']), 576.516685202, 151.219277482, 511035, 5.6e-05), alg_cluster.Cluster(set(['27003']), 573.942484199, 145.118314377, 298084, 4.6e-05), alg_cluster.Cluster(set(['27053']), 570.131597541, 151.403325043, 1116200, 5.8e-05), alg_cluster.Cluster(set(['29095']), 558.451289477, 291.559180265, 654880, 4.6e-05), alg_cluster.Cluster(set(['29189', '29183', '29510']), 629.290698203, 296.864280474, 1648387, 5.96622285907e-05), alg_cluster.Cluster(set(['28043']), 647.649972548, 410.394464547, 23263, 4.7e-05), alg_cluster.Cluster(set(['28087']), 674.418402473, 415.122758999, 61586, 4.6e-05), alg_cluster.Cluster(set(['28033']), 642.267628251, 384.839249499, 107199, 4.6e-05), alg_cluster.Cluster(set(['28027']), 631.700027283, 400.68741948, 30622, 6e-05), alg_cluster.Cluster(set(['28159']), 663.514261498, 425.274137823, 20160, 5.9e-05), alg_cluster.Cluster(set(['28089']), 644.644674143, 437.339606833, 74674, 4.6e-05), alg_cluster.Cluster(set(['28121']), 647.272159578, 445.553667274, 115327, 4.8e-05), alg_cluster.Cluster(set(['28049']), 638.051593606, 445.785870317, 250800, 6e-05), alg_cluster.Cluster(set(['28075']), 672.167227537, 440.608524349, 78161, 4.6e-05), alg_cluster.Cluster(set(['28035']), 662.340841725, 469.562070989, 72604, 5e-05), alg_cluster.Cluster(set(['37071']), 806.573724958, 356.877472978, 190365, 4.8e-05), alg_cluster.Cluster(set(['37119']), 813.724315147, 356.853362811, 695454, 5.6e-05), alg_cluster.Cluster(set(['37057']), 823.18698731, 342.886324895, 147246, 4.6e-05), alg_cluster.Cluster(set(['37025']), 818.35071393, 352.864665547, 131063, 4.7e-05), alg_cluster.Cluster(set(['37081']), 829.726844142, 334.637483646, 421048, 4.8e-05), alg_cluster.Cluster(set(['31153', '31055']), 526.064238683, 239.067607287, 586180, 5.9281150841e-05), alg_cluster.Cluster(set(['31109']), 516.78216337, 250.188023316, 250291, 6.1e-05), alg_cluster.Cluster(set(['33011']), 936.826960243, 147.991772374, 380841, 5e-05), alg_cluster.Cluster(set(['36005', '34013', '34017', '36061', '36081', '36047', '36085', '34039']), 911.004570517, 207.361438421, 9933427, 0.000100484812543), alg_cluster.Cluster(set(['34003', '34031']), 906.566100671, 202.092249843, 1373167, 6.68631193438e-05), alg_cluster.Cluster(set(['34023']), 904.976453741, 215.001458637, 750162, 5.9e-05), alg_cluster.Cluster(set(['34021']), 900.837767215, 220.161475984, 350761, 4.6e-05), alg_cluster.Cluster(set(['34007', '34005']), 901.166479588, 230.851687237, 932326, 5.20046078303e-05), alg_cluster.Cluster(set(['32003']), 178.153492162, 324.160586278, 1375765, 4.9e-05), alg_cluster.Cluster(set(['36001']), 900.893220363, 164.489226174, 294565, 4.9e-05), alg_cluster.Cluster(set(['36029']), 820.38582573, 177.013330392, 950265, 5e-05), alg_cluster.Cluster(set(['36119', '36087']), 911.127770674, 196.82648364, 1210212, 6.12088890211e-05), alg_cluster.Cluster(set(['36059']), 917.384980291, 205.43647538, 1334544, 7.6e-05), alg_cluster.Cluster(set(['36103']), 929.241649488, 199.278463003, 1419369, 6.3e-05), alg_cluster.Cluster(set(['36079']), 910.914101605, 190.332224, 95745, 4.8e-05), alg_cluster.Cluster(set(['36083']), 907.985922231, 160.259081442, 152538, 4.7e-05), alg_cluster.Cluster(set(['39087']), 770.625409557, 283.93917465, 62319, 4.6e-05), alg_cluster.Cluster(set(['39017']), 731.844357783, 269.494670001, 332807, 4.9e-05), alg_cluster.Cluster(set(['39049']), 758.062157993, 253.603273009, 1068978, 5.2e-05), alg_cluster.Cluster(set(['39035']), 776.351457758, 216.558042612, 1393978, 5.8e-05), alg_cluster.Cluster(set(['39095']), 742.473618138, 216.811437951, 455054, 4.6e-05), alg_cluster.Cluster(set(['40121']), 534.015957707, 386.972736212, 43953, 5.2e-05), alg_cluster.Cluster(set(['40143']), 529.254373189, 359.119882043, 563299, 5.1e-05), alg_cluster.Cluster(set(['41029']), 78.4141193387, 147.629027207, 181269, 5.1e-05), alg_cluster.Cluster(set(['41047']), 97.399304684, 93.4988892144, 284834, 4.8e-05), alg_cluster.Cluster(set(['41005']), 103.421444616, 88.318590492, 338391, 6.6e-05), alg_cluster.Cluster(set(['53011', '41051']), 103.536318033, 77.6310109522, 1005724, 8.30450799623e-05), alg_cluster.Cluster(set(['41067']), 92.2254623376, 76.2593957841, 445342, 7.3e-05), alg_cluster.Cluster(set(['42045', '42101']), 893.695541169, 228.802539398, 2068414, 5.64020684447e-05), alg_cluster.Cluster(set(['42003']), 809.003419092, 233.899638663, 1281666, 6.1e-05), alg_cluster.Cluster(set(['42011']), 878.575486588, 221.678319842, 373638, 4.6e-05), alg_cluster.Cluster(set(['45003']), 804.805415327, 398.777010123, 142552, 4.8e-05), alg_cluster.Cluster(set(['45063']), 810.799412401, 389.504491524, 216014, 4.8e-05), alg_cluster.Cluster(set(['45079']), 816.541641816, 385.156707247, 320677, 5.4e-05), alg_cluster.Cluster(set(['45007']), 782.226804679, 379.132979851, 165740, 4.6e-05), alg_cluster.Cluster(set(['45091']), 807.886971209, 364.469906345, 164614, 4.7e-05), alg_cluster.Cluster(set(['45083']), 793.239375577, 367.754402204, 253791, 4.8e-05), alg_cluster.Cluster(set(['45045']), 785.676714035, 369.542097768, 379616, 5.2e-05), alg_cluster.Cluster(set(['51520', '47163']), 782.658124983, 331.313567482, 170415, 4.79171903882e-05), alg_cluster.Cluster(set(['47053']), 660.602484901, 357.318624524, 48152, 4.6e-05), alg_cluster.Cluster(set(['47157']), 643.395763039, 378.031744605, 897472, 5.5e-05), alg_cluster.Cluster(set(['47149']), 707.710145119, 356.803460768, 182023, 5e-05), alg_cluster.Cluster(set(['47037']), 700.009323976, 350.107265446, 569891, 6.1e-05), alg_cluster.Cluster(set(['47165']), 705.571676152, 342.569345394, 130449, 4.6e-05), alg_cluster.Cluster(set(['47065']), 732.643747577, 370.017730905, 307896, 6.1e-05), alg_cluster.Cluster(set(['47093']), 753.012743594, 348.235180569, 382032, 5.6e-05), alg_cluster.Cluster(set(['48003']), 398.962651077, 443.958242671, 13004, 5.3e-05), alg_cluster.Cluster(set(['48029']), 477.886663525, 514.095891984, 1392931, 5e-05), alg_cluster.Cluster(set(['48157']), 533.434165736, 513.008691943, 354452, 4.6e-05), alg_cluster.Cluster(set(['48201']), 540.54731652, 504.62993865, 3400578, 6e-05), alg_cluster.Cluster(set(['48245']), 565.746895809, 504.541799993, 252051, 5.7e-05), alg_cluster.Cluster(set(['48361']), 571.064681764, 498.867855628, 84966, 4.6e-05), alg_cluster.Cluster(set(['48453']), 493.032076052, 493.597339677, 812280, 5.2e-05), alg_cluster.Cluster(set(['48041']), 522.88823653, 487.351397054, 152415, 4.6e-05), alg_cluster.Cluster(set(['48439']), 503.673815634, 437.477028749, 1446219, 5e-05), alg_cluster.Cluster(set(['48113']), 513.657901701, 437.682966844, 2218899, 5.4e-05), alg_cluster.Cluster(set(['48365']), 562.161603376, 451.397747537, 22756, 4.8e-05), alg_cluster.Cluster(set(['48183']), 552.333188086, 444.322743975, 111379, 5.5e-05), alg_cluster.Cluster(set(['48423']), 542.731029941, 446.457985602, 174706, 4.7e-05), alg_cluster.Cluster(set(['48203']), 560.270010669, 442.325574621, 62110, 5e-05), alg_cluster.Cluster(set(['48085']), 517.70778434, 427.895646823, 491675, 4.8e-05), alg_cluster.Cluster(set(['51640']), 806.823088186, 324.555032883, 6837, 5.2e-05), alg_cluster.Cluster(set(['51750']), 811.690750985, 312.898714856, 15859, 4.6e-05), alg_cluster.Cluster(set(['51510', '11001', '51013', '24033']), 868.773385157, 261.367545904, 1691310, 7.01566407105e-05), alg_cluster.Cluster(set(['51775', '51161', '51770']), 821.105453327, 307.678349369, 205436, 5.95638203625e-05), alg_cluster.Cluster(set(['51690']), 826.020074281, 321.016553783, 15416, 4.9e-05), alg_cluster.Cluster(set(['51590']), 834.603738103, 321.684114822, 48411, 4.8e-05), alg_cluster.Cluster(set(['51680']), 835.264653899, 302.326633095, 65269, 5.8e-05), alg_cluster.Cluster(set(['51515']), 829.535165128, 304.77544828, 6299, 4.7e-05), alg_cluster.Cluster(set(['51820']), 837.346467474, 285.851438947, 19520, 5.8e-05), alg_cluster.Cluster(set(['51540']), 845.239184424, 285.286609195, 45049, 5.4e-05), alg_cluster.Cluster(set(['51660']), 836.595959983, 277.430066898, 40468, 5.2e-05), alg_cluster.Cluster(set(['51730', '51570', '51670']), 868.870650188, 299.725931421, 72991, 5.47692455234e-05), alg_cluster.Cluster(set(['51840']), 845.843602685, 258.214178983, 23585, 7.1e-05), alg_cluster.Cluster(set(['51595']), 868.072034995, 313.157738101, 5665, 4.8e-05), alg_cluster.Cluster(set(['51700', '51650', '51710']), 888.137574448, 301.733598622, 560990, 4.72535143229e-05), alg_cluster.Cluster(set(['51087', '51041', '51760']), 865.533206632, 294.750713222, 719993, 6.53475742125e-05), alg_cluster.Cluster(set(['51630']), 861.833345286, 275.583093594, 19279, 4.8e-05), alg_cluster.Cluster(set(['51683', '51685', '51600', '51610', '51059', '51153']), 862.243679441, 263.263769009, 1327862, 5.50028557184e-05), alg_cluster.Cluster(set(['51107']), 855.815074611, 258.409034617, 169599, 4.9e-05), alg_cluster.Cluster(set(['51085']), 864.408961095, 288.394572842, 86320, 4.6e-05), alg_cluster.Cluster(set(['53033']), 125.27486023, 39.1497730391, 1737034, 5.8e-05), alg_cluster.Cluster(set(['55025']), 640.259029023, 193.059886956, 426526, 5.2e-05), alg_cluster.Cluster(set(['55079', '55133']), 663.251735605, 192.55282564, 1300931, 6.70671380727e-05), alg_cluster.Cluster(set(['55009']), 661.295442891, 158.436859333, 226778, 5.2e-05), alg_cluster.Cluster(set(['55087']), 653.76289252, 160.48762926, 160971, 4.6e-05), alg_cluster.Cluster(set(['54039']), 789.786928856, 287.714693693, 200073, 4.8e-05), alg_cluster.Cluster(set(['54009']), 799.221537984, 240.153315109, 25447, 7.7e-05)])
    print "Expected: (5.9860404338743436, 86, 88)"
    print "\nTest 5...."
    print prj3.fast_closest_pair([alg_cluster.Cluster(set(['01101']), 720.281573781, 440.436162917, 223510, 5.7e-05), alg_cluster.Cluster(set(['01121', '01015', '01055', '01115']), 719.648599349, 404.839801183, 360771, 5.08190458767e-05), alg_cluster.Cluster(set(['01073', '01117']), 705.081266116, 412.149814394, 805340, 6.99752141952e-05), alg_cluster.Cluster(set(['01125']), 692.900099393, 417.773844647, 164875, 5.4e-05), alg_cluster.Cluster(set(['01103', '01089']), 706.416636666, 384.576211909, 387764, 5.15728432758e-05), alg_cluster.Cluster(set(['01033', '01077']), 685.447113541, 382.760589081, 142950, 4.6e-05), alg_cluster.Cluster(set(['01113', '13215', '01081']), 741.629139512, 431.599214626, 351139, 5.56249946602e-05), alg_cluster.Cluster(set(['05119']), 598.676543754, 389.524749021, 361474, 5.3e-05), alg_cluster.Cluster(set(['05139']), 595.14987863, 427.226433206, 45629, 5.4e-05), alg_cluster.Cluster(set(['04013']), 214.128077618, 396.893960776, 3072149, 6.8e-05), alg_cluster.Cluster(set(['06025']), 156.397958859, 393.161127277, 142361, 5.6e-05), alg_cluster.Cluster(set(['06065']), 146.410389633, 374.21707964, 1545387, 6.1e-05), alg_cluster.Cluster(set(['06073']), 129.2075529, 387.064888184, 2813833, 6.6e-05), alg_cluster.Cluster(set(['06059']), 113.997715586, 368.503452566, 2846289, 9.8e-05), alg_cluster.Cluster(set(['06037']), 105.369854549, 359.050126004, 9519338, 0.00011), alg_cluster.Cluster(set(['06111']), 93.4973310868, 344.590570899, 753197, 5.8e-05), alg_cluster.Cluster(set(['06083']), 76.0382837186, 340.420376302, 399347, 6.4e-05), alg_cluster.Cluster(set(['06029']), 103.787886113, 326.006585349, 661645, 9.7e-05), alg_cluster.Cluster(set(['06071']), 148.402461892, 350.061039619, 1709434, 7.7e-05), alg_cluster.Cluster(set(['06027']), 136.048381588, 306.102582286, 17945, 5.3e-05), alg_cluster.Cluster(set(['06107']), 108.085024898, 306.351832438, 368021, 5.8e-05), alg_cluster.Cluster(set(['06031']), 89.2713893096, 304.772281089, 129461, 5.1e-05), alg_cluster.Cluster(set(['06019', '06039']), 95.8235848204, 288.669728653, 922516, 6.34662032962e-05), alg_cluster.Cluster(set(['06047']), 80.1217093401, 275.749681794, 210554, 4.7e-05), alg_cluster.Cluster(set(['06081', '06013', '06075', '06001']), 58.5247340469, 257.444458761, 3876451, 6.53559810249e-05), alg_cluster.Cluster(set(['06085']), 63.1509653633, 270.516712105, 1682585, 6.3e-05), alg_cluster.Cluster(set(['06099', '06077']), 75.6870842456, 260.385338121, 1010595, 5.15576892821e-05), alg_cluster.Cluster(set(['06067', '06095', '06113']), 71.5249492655, 244.643706918, 1786701, 5.74988825774e-05), alg_cluster.Cluster(set(['06061']), 90.0298511972, 233.575536165, 248399, 5.2e-05), alg_cluster.Cluster(set(['06115', '06101']), 77.5317480757, 227.828263605, 139149, 5.29706357933e-05), alg_cluster.Cluster(set(['06007']), 79.7767444918, 214.910128237, 203171, 4.7e-05), alg_cluster.Cluster(set(['06021']), 65.2043358182, 213.245337355, 26453, 6.9e-05), alg_cluster.Cluster(set(['06089']), 77.359494209, 188.945068958, 163256, 5.7e-05), alg_cluster.Cluster(set(['08005', '08001']), 380.140193285, 268.051898162, 851824, 6.19900531096e-05), alg_cluster.Cluster(set(['08059', '08031']), 367.756092129, 268.823872427, 1081692, 6.73059650991e-05), alg_cluster.Cluster(set(['25013', '09003', '09013', '25015']), 926.23044241, 173.525384291, 1602026, 5.39348506204e-05), alg_cluster.Cluster(set(['09007', '09001', '09005', '36079', '09009']), 920.921406597, 188.591324722, 2139584, 5.25906568754e-05), alg_cluster.Cluster(set(['10003']), 888.26796027, 239.785084878, 500265, 4.9e-05), alg_cluster.Cluster(set(['12071']), 822.736368501, 559.319167615, 440888, 4.7e-05), alg_cluster.Cluster(set(['12086']), 855.717845944, 576.450702277, 2253362, 4.9e-05), alg_cluster.Cluster(set(['12011', '12099']), 853.730086097, 559.565110381, 2754202, 5.04107120683e-05), alg_cluster.Cluster(set(['12057']), 810.083518173, 529.957501469, 998948, 4.7e-05), alg_cluster.Cluster(set(['12095', '12117']), 828.826823208, 511.667716297, 1261540, 5.11315471566e-05), alg_cluster.Cluster(set(['12031', '12019']), 814.780076149, 474.403030262, 919693, 4.85406706368e-05), alg_cluster.Cluster(set(['13087', '13275', '12073', '12065']), 763.050120815, 475.121973756, 323331, 5.86001991767e-05), alg_cluster.Cluster(set(['12023']), 796.544243535, 477.588016437, 56513, 5e-05), alg_cluster.Cluster(set(['13095']), 761.086378978, 451.967184234, 96065, 4.9e-05), alg_cluster.Cluster(set(['13295', '13313', '13047', '47065']), 733.484444335, 373.203402996, 505756, 5.81703786015e-05), alg_cluster.Cluster(set(['13285', '13077']), 743.86305095, 414.529710034, 147994, 4.7e-05), alg_cluster.Cluster(set(['13015', '13115', '13129']), 738.332250372, 389.376319118, 210688, 5.01380809538e-05), alg_cluster.Cluster(set(['13021', '13153']), 768.214107465, 424.559788215, 264652, 5.06517540015e-05), alg_cluster.Cluster(set(['13255', '13089', '13297', '13067', '13113', '13063', '13151', '13217', '13097', '13135', '13117', '13013', '13121', '13247', '13223', '13045', '13057']), 752.25609213, 399.429308569, 3923981, 6.26635776269e-05), alg_cluster.Cluster(set(['13219', '13059']), 770.124456082, 394.603787436, 127714, 5.17679502639e-05), alg_cluster.Cluster(set(['13073', '45003', '13245']), 798.617284904, 401.765590433, 431615, 5.35051399975e-05), alg_cluster.Cluster(set(['19163', '17161']), 622.251364027, 229.337743865, 308042, 5.30905136313e-05), alg_cluster.Cluster(set(['19153']), 570.801738263, 228.668095362, 374601, 5.2e-05), alg_cluster.Cluster(set(['19013']), 591.836020306, 209.588448378, 128012, 4.6e-05), alg_cluster.Cluster(set(['19057']), 612.882010424, 244.949915243, 42351, 5.1e-05), alg_cluster.Cluster(set(['17031', '17043']), 668.403256539, 219.438581907, 6280902, 5.95604599467e-05), alg_cluster.Cluster(set(['17201']), 645.722085, 209.852492823, 278418, 4.8e-05), alg_cluster.Cluster(set(['18089']), 677.840033419, 228.268571284, 484564, 4.8e-05), alg_cluster.Cluster(set(['18097']), 703.47637833, 264.614798668, 860454, 4.8e-05), alg_cluster.Cluster(set(['20173']), 502.059178492, 322.563937328, 452869, 5.1e-05), alg_cluster.Cluster(set(['20091', '29095', '20209']), 554.441297852, 292.348314084, 1263848, 4.80522673613e-05), alg_cluster.Cluster(set(['39087', '21019']), 769.782444768, 286.749880974, 112071, 5.13271943679e-05), alg_cluster.Cluster(set(['21067']), 738.000675961, 302.005037855, 260512, 4.8e-05), alg_cluster.Cluster(set(['39017', '21117', '39061']), 732.999953584, 274.525113628, 1329574, 5.229276821e-05), alg_cluster.Cluster(set(['21111']), 715.347723878, 301.167740487, 693604, 5.9e-05), alg_cluster.Cluster(set(['22017', '22015']), 572.234109108, 441.521371486, 350471, 5.83533930054e-05), alg_cluster.Cluster(set(['22121', '22047', '22033']), 626.917502008, 487.4986862, 467773, 5.25264348306e-05), alg_cluster.Cluster(set(['22051', '22071', '22095']), 648.907302448, 500.185107939, 983184, 5.50922472294e-05), alg_cluster.Cluster(set(['25025', '25017', '25021']), 946.353690987, 158.342897287, 2805511, 5.87468699998e-05), alg_cluster.Cluster(set(['24001']), 834.528507681, 249.862506444, 74930, 4.8e-05), alg_cluster.Cluster(set(['24043', '51840', '24021', '51107']), 854.525807773, 251.76709922, 520384, 4.96118135838e-05), alg_cluster.Cluster(set(['24025', '24510', '24005']), 872.961611864, 247.553326141, 1624036, 6.41933725607e-05), alg_cluster.Cluster(set(['26163', '26125', '26099']), 746.212398845, 196.1083948, 4043467, 5.93987434546e-05), alg_cluster.Cluster(set(['27123', '27053', '27003']), 572.416396897, 150.381408226, 1925319, 5.5611264419e-05), alg_cluster.Cluster(set(['29189', '29183', '29510']), 629.290698203, 296.864280474, 1648387, 5.96622285907e-05), alg_cluster.Cluster(set(['28043']), 647.649972548, 410.394464547, 23263, 4.7e-05), alg_cluster.Cluster(set(['28087']), 674.418402473, 415.122758999, 61586, 4.6e-05), alg_cluster.Cluster(set(['28033', '47157']), 643.275390379, 378.758109472, 1004671, 5.40396945866e-05), alg_cluster.Cluster(set(['28027']), 631.700027283, 400.68741948, 30622, 6e-05), alg_cluster.Cluster(set(['28159']), 663.514261498, 425.274137823, 20160, 5.9e-05), alg_cluster.Cluster(set(['28049', '28121', '28089']), 641.580877586, 444.294277603, 440801, 5.44887602342e-05), alg_cluster.Cluster(set(['28075']), 672.167227537, 440.608524349, 78161, 4.6e-05), alg_cluster.Cluster(set(['28035']), 662.340841725, 469.562070989, 72604, 5e-05), alg_cluster.Cluster(set(['37025', '45091', '37119', '37071']), 812.272104617, 357.475970759, 1181496, 5.24587158992e-05), alg_cluster.Cluster(set(['37057', '37081']), 828.032355446, 336.774773286, 568294, 4.74817963941e-05), alg_cluster.Cluster(set(['31153', '31055']), 526.064238683, 239.067607287, 586180, 5.9281150841e-05), alg_cluster.Cluster(set(['31109']), 516.78216337, 250.188023316, 250291, 6.1e-05), alg_cluster.Cluster(set(['33011']), 936.826960243, 147.991772374, 380841, 5e-05), alg_cluster.Cluster(set(['36005', '34003', '34013', '34017', '36119', '34031', '36061', '36081', '36059', '36047', '36085', '34039', '36087']), 911.190059698, 205.733152915, 13851350, 9.13610482011e-05), alg_cluster.Cluster(set(['34021', '34023']), 903.657842154, 216.645472655, 1100923, 5.48581181427e-05), alg_cluster.Cluster(set(['34005', '34007', '42045', '42101']), 896.016751981, 229.439206956, 3000740, 5.50357831735e-05), alg_cluster.Cluster(set(['32003']), 178.153492162, 324.160586278, 1375765, 4.9e-05), alg_cluster.Cluster(set(['36001', '36083']), 903.313035389, 163.046028931, 447103, 4.83176605838e-05), alg_cluster.Cluster(set(['36029']), 820.38582573, 177.013330392, 950265, 5e-05), alg_cluster.Cluster(set(['36103']), 929.241649488, 199.278463003, 1419369, 6.3e-05), alg_cluster.Cluster(set(['39049']), 758.062157993, 253.603273009, 1068978, 5.2e-05), alg_cluster.Cluster(set(['39035']), 776.351457758, 216.558042612, 1393978, 5.8e-05), alg_cluster.Cluster(set(['39095']), 742.473618138, 216.811437951, 455054, 4.6e-05), alg_cluster.Cluster(set(['40121']), 534.015957707, 386.972736212, 43953, 5.2e-05), alg_cluster.Cluster(set(['40143']), 529.254373189, 359.119882043, 563299, 5.1e-05), alg_cluster.Cluster(set(['41029']), 78.4141193387, 147.629027207, 181269, 5.1e-05), alg_cluster.Cluster(set(['41047', '41005']), 100.669131719, 90.6861547044, 623225, 5.77734173051e-05), alg_cluster.Cluster(set(['53011', '41051', '41067']), 100.064939683, 77.2100529516, 1451066, 7.99621767721e-05), alg_cluster.Cluster(set(['42003', '54009']), 808.812984502, 234.02138583, 1307113, 6.13114895193e-05), alg_cluster.Cluster(set(['42011']), 878.575486588, 221.678319842, 373638, 4.6e-05), alg_cluster.Cluster(set(['45063', '45079']), 814.230438638, 386.906656981, 536691, 5.15850461439e-05), alg_cluster.Cluster(set(['45007', '45083', '45045']), 787.362946304, 370.963478004, 799147, 4.94853137157e-05), alg_cluster.Cluster(set(['51520', '47163']), 782.658124983, 331.313567482, 170415, 4.79171903882e-05), alg_cluster.Cluster(set(['47053']), 660.602484901, 357.318624524, 48152, 4.6e-05), alg_cluster.Cluster(set(['47149', '47037', '47165']), 702.420270317, 350.374216155, 882363, 5.65131980829e-05), alg_cluster.Cluster(set(['47093']), 753.012743594, 348.235180569, 382032, 5.6e-05), alg_cluster.Cluster(set(['48003']), 398.962651077, 443.958242671, 13004, 5.3e-05), alg_cluster.Cluster(set(['48029']), 477.886663525, 514.095891984, 1392931, 5e-05), alg_cluster.Cluster(set(['48201', '48157']), 539.875878337, 505.420842015, 3755030, 5.86784851253e-05), alg_cluster.Cluster(set(['48245', '48361']), 567.08757299, 503.111331035, 337017, 5.4226768976e-05), alg_cluster.Cluster(set(['48453']), 493.032076052, 493.597339677, 812280, 5.2e-05), alg_cluster.Cluster(set(['48041']), 522.88823653, 487.351397054, 152415, 4.6e-05), alg_cluster.Cluster(set(['48113', '48439']), 509.718280939, 437.601705726, 3665118, 5.24216399035e-05), alg_cluster.Cluster(set(['48203', '48365', '48183']), 555.98480453, 444.511052429, 196245, 5.26058396392e-05), alg_cluster.Cluster(set(['48423']), 542.731029941, 446.457985602, 174706, 4.7e-05), alg_cluster.Cluster(set(['48085']), 517.70778434, 427.895646823, 491675, 4.8e-05), alg_cluster.Cluster(set(['51640']), 806.823088186, 324.555032883, 6837, 5.2e-05), alg_cluster.Cluster(set(['51775', '51161', '51750', '51770']), 820.430753201, 308.052464357, 221295, 5.8591775684e-05), alg_cluster.Cluster(set(['51590', '51690']), 832.530543977, 321.522880219, 63827, 4.82415278801e-05), alg_cluster.Cluster(set(['51680', '51515']), 834.76037755, 302.542163595, 71568, 5.70318438408e-05), alg_cluster.Cluster(set(['51820', '51660', '51540']), 840.442400038, 282.36465715, 105037, 5.39728095814e-05), alg_cluster.Cluster(set(['51087', '51085', '51760', '51730', '51041', '51570', '51670']), 865.699882171, 294.539732849, 879304, 6.2570144114e-05), alg_cluster.Cluster(set(['51595']), 868.072034995, 313.157738101, 5665, 4.8e-05), alg_cluster.Cluster(set(['51700', '51650', '51710']), 888.137574448, 301.733598622, 560990, 4.72535143229e-05), alg_cluster.Cluster(set(['51630']), 861.833345286, 275.583093594, 19279, 4.8e-05), alg_cluster.Cluster(set(['24003', '11001', '24033', '24031', '51013', '51059', '51510', '51683', '51685', '24027', '51600', '51610', '51153']), 866.342018296, 259.888193978, 4630011, 6.24798262898e-05), alg_cluster.Cluster(set(['53033']), 125.27486023, 39.1497730391, 1737034, 5.8e-05), alg_cluster.Cluster(set(['55025']), 640.259029023, 193.059886956, 426526, 5.2e-05), alg_cluster.Cluster(set(['55079', '55133']), 663.251735605, 192.55282564, 1300931, 6.70671380727e-05), alg_cluster.Cluster(set(['55009', '55087']), 658.168362832, 159.288220615, 387749, 4.95091463808e-05), alg_cluster.Cluster(set(['54039']), 789.786928856, 287.714693693, 200073, 4.8e-05)])
    print "Expected: (12.40813868786967, 33, 34)"
    
    
    
    
    