'''Module providing functions of drawing'''

def set_gradient():
    first_color = color(169, 186, 222)
    second_color = color(227, 192, 196)
    third_color = color(181, 180, 202)
    gradient_border = 240
    gradient_end = 395
    amt = 0
    for i in range(gradient_border):
        stroke(lerpColor(first_color, second_color, amt))
        line(0, i, width, i)
        amt += 0.008
    amt = 0
    for i in range(gradient_border, gradient_end):
        stroke(lerpColor(second_color, third_color, amt))
        line(0, i, width, i)
        amt += 0.008
        

def set_sand():
    fill(209, 172, 117)
    stroke(108, 58, 10)

    ''' Left side sand '''
    beginShape()
    strokeWeight(3)
    curveVertex(0, 405)
    curveVertex(0, 405)
    curveVertex(300, 380)
    curveVertex(300, 380)
    endShape()

    ''' Right side sand '''
    beginShape()
    strokeWeight(2)
    curveVertex(537, 360)
    curveVertex(537, 360)
    curveVertex(925, 365)
    curveVertex(width, 368)
    curveVertex(width, 368)
    vertex(width, 368)
    vertex(width, height)
    vertex(0, height)
    vertex(0, 405)
    endShape()


def set_grass_field():
    fill(103, 160, 115)
    noStroke()
    beginShape()
    vertex(0, 405)
    vertex(0, 370)
    curveVertex(0, 370)
    curveVertex(0, 370)
    curveVertex(300, 380)
    curveVertex(0, 435)
    curveVertex(0, 435)
    vertex(0, 435)
    endShape()


def draw_krosh():
    fill(144, 215, 209)
    stroke(36, 135, 159)
    strokeWeight(6)

    ''' Left Krosh`s ear '''
    beginShape()
    curveVertex(455, 282)
    curveVertex(455, 282)
    curveVertex(469, 254)
    curveVertex(469, 202)
    curveVertex(459, 168)
    curveVertex(446, 130)
    curveVertex(447, 96)
    curveVertex(460, 80)
    curveVertex(486, 86)
    curveVertex(510, 118)
    curveVertex(522, 158)
    curveVertex(519, 202)
    curveVertex(508, 242)
    curveVertex(494, 269)
    curveVertex(478, 291)
    curveVertex(478, 291)
    endShape()

    ''' Right Krosh`s leg '''
    beginShape()
    curveVertex(347, 470)
    curveVertex(347, 470)
    curveVertex(314, 484)
    curveVertex(293, 503)
    curveVertex(287, 523)
    curveVertex(295, 530)
    curveVertex(306, 530)
    curveVertex(377, 514)
    curveVertex(379, 485)
    curveVertex(379, 485)
    endShape()

    ''' Left Krosh`s leg '''
    beginShape()
    curveVertex(415, 495)
    curveVertex(415, 495)
    curveVertex(413, 507)
    curveVertex(420, 520)
    curveVertex(435, 524)
    curveVertex(500, 523)
    curveVertex(515, 516)
    curveVertex(510, 501)
    curveVertex(487, 484)
    curveVertex(487, 484)
    endShape()

    ''' Left Krosh`s hand '''
    beginShape()
    curveVertex(507, 468)
    curveVertex(507, 468)
    curveVertex(538, 478)
    curveVertex(561, 471)
    curveVertex(567, 450)
    curveVertex(552, 438)
    curveVertex(532, 435)
    curveVertex(532, 435)
    endShape()

    ''' Krosh`s body '''
    ellipse(422, 385, 247, 225)

    ''' Right Krosh`s ear '''
    beginShape()
    curveVertex(412, 286)
    curveVertex(412, 286)
    curveVertex(418, 266)
    curveVertex(410, 218)
    curveVertex(380, 176)
    curveVertex(348, 140)
    curveVertex(332, 112)
    curveVertex(334, 92)
    curveVertex(357, 77)
    curveVertex(399, 90)
    curveVertex(436, 133)
    curveVertex(453, 186)
    curveVertex(457, 232)
    curveVertex(450, 267)
    curveVertex(445, 282)
    curveVertex(445, 282)
    endShape()

    ''' Right Krosh`s hand '''
    beginShape()
    curveVertex(343, 389)
    curveVertex(343, 389)
    curveVertex(327, 386)
    curveVertex(301, 394)
    curveVertex(281, 411)
    curveVertex(269, 444)
    curveVertex(291, 462)
    curveVertex(313, 436)
    curveVertex(322, 422)
    curveVertex(341, 402)
    curveVertex(343, 389)
    curveVertex(343, 389)
    endShape()

    ''' Krosh`s face '''
    beginShape()
    strokeWeight(4)
    curveVertex(486, 331)
    curveVertex(486, 331)
    curveVertex(495, 342)
    curveVertex(501, 361)
    curveVertex(496, 395)
    curveVertex(501, 370)
    curveVertex(502, 386)
    curveVertex(502, 386)
    endShape()
    
    ''' Krosh`s right eye '''
    fill(233, 233 , 231)
    beginShape()
    curveVertex(501, 361)
    curveVertex(501, 361)
    curveVertex(479, 351)
    curveVertex(459, 351)
    curveVertex(447, 353)
    curveVertex(446, 363)
    curveVertex(447, 380)
    curveVertex(455, 397)
    curveVertex(468, 407)
    curveVertex(479, 408)
    curveVertex(495, 397)
    curveVertex(501, 382)
    curveVertex(501, 361)
    curveVertex(501, 361)
    endShape()


    # TODO: Krosh`s body shadows
    pass

    # TODO: Krosh`s ground shadow
    pass

    ''' Krosh`s nose '''
    fill(224, 56, 100)
    noStroke()
    circle(509, 398, 25)


# TODO: EZHIK
def draw_ezhik():
    ''' Ezhik`s spikes '''
    stroke(68, 18, 86)
    strokeWeight(5)
    beginShape()
    fill(94, 51, 123)
    vertex(612, 420)
    vertex(547, 361)
    vertex(594, 324)
    vertex(581, 257)
    vertex(660, 268)
    vertex(699, 199)
    vertex(747, 257)
    vertex(812, 230)
    vertex(810, 300)
    vertex(870, 320)
    vertex(824, 398)
    endShape()
    

    # KOCTbIJlu
    fill(190, 77, 123)
    strokeWeight(6)
    noStroke()
    ellipse(715, 392, 217, 210)
    
    fill(94, 51, 123)
    rect(705, 280, 40, 17)

    fill(190, 77, 123)
    stroke(128,15,62)

    ''' Ezhik`s body '''
    beginShape()
    curveVertex(612, 418)
    curveVertex(612, 418)
    curveVertex(608, 398)
    curveVertex(609, 376)
    curveVertex(612, 357)
    curveVertex(612, 357)
    endShape()

    # Right ear
    bezier(612, 357, 584, 363, 600, 307, 623, 336)
    
    bezier(623, 336, 635, 299, 695, 275, 718, 297)
    bezier(718, 297, 743, 275, 790, 299, 802, 329)
    
    # Left ear
    bezier(802, 329, 837, 317, 835, 360, 816, 355)
    bezier(816, 355, 850, 470, 720, 520, 678, 493)
    bezier(612, 418, 615, 443, 648, 479, 674, 484)
    curve(678, 493, 678, 493, 674, 484, 690, 484)
