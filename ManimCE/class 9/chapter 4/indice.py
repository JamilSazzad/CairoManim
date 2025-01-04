
from manim import *

# To watch one of these scenes, run the following:
#manim -pql indice.py IndiceIntro
#manim -pqm basic.py JustifyText
#
# Use the flag --quality l for a faster rendering at a lower quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have preview of the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the nth animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1920,1080
# for a 1920x1080 video)
myTemplate = TexTemplate(tex_compiler="xelatex", output_format=".xdv", preamble=r"\usepackage[banglamainfont=Kalpurush, banglattfont=Kalpurush]{latexbangla}")

class Kross(VGroup):
    CONFIG = {
        "stroke_color": RED,
        "stroke_width": 6,
    }

    def __init__(self, mobject, **kwargs):
        VGroup.__init__(self,
                        #Line(UP + LEFT, DOWN + RIGHT),
                        Line(UP + RIGHT, DOWN + LEFT),
                        )
        self.replace(mobject, stretch=True)
        self.set_stroke(RED, self.stroke_width)



# class Kross_Test(Scene):
# 	def construct(self):
# 		scale=2
# 		five=MathTex("5").scale(scale)
# 		plus=MathTex("+").scale(scale)
# 		add=VGroup(five,plus,five.copy(),plus.copy(),five.copy(),plus.copy(),five.copy()).arrange(RIGHT)
# 		self.play(Write(add))
# 		self.wait(3)
# 		b=Kross(add)
# 		self.add(b)
# 		self.wait(3)
def index_label(mobject, label_height=0.15):
    labels = VGroup()
    for n, submob in enumerate(mobject):
        label = Integer(n)
        label.set_height(label_height)
        label.move_to(submob)
        label.set_stroke(PINK, 0.5, background=False)
        labels.add(label)
    return labels

class Eq(VGroup):
    def __init__(self, tex,**kwargs):
        self.formula=tex
    def get_slice(self,*indices):
        return VGroup(*[self.formula[i] for i in indices])

class Test(Scene):
    def construct(self):
        tex_1=MathTex("x^2+2xy+y^2",substrings_to_isolate=["+","^"]).scale(2).move_to(UP)
        tex_2=MathTex("x^2+y^2+2xy",substrings_to_isolate=["+","^"]).next_to(tex_1,DOWN*3).scale(2)
        a=Eq(tex_1)
        b=Eq(tex_2)
        self.play(FadeIn(tex_1))
        self.wait()
        self.play(TransformFromCopy(a.get_slice(0,2,5,6,8),b.get_slice(0,2,3,4,6)))
        self.add(index_label(tex_1),index_label(tex_2))
        self.wait(2)
        self.play(TransformFromCopy(a.get_slice(3,4),b.get_slice(7,8)))
        self.wait(2)


class Intro1(Scene):
	def construct(self):
		scale=1.8
		eq=MathTex("=").scale(scale)
		two=MathTex("2").scale(scale)
		three=MathTex("3").scale(scale)
		plus=MathTex("+").scale(scale)
		times=MathTex(r"\times").scale(scale)
		a_group=VGroup(two.copy(),plus.copy(),two.copy(),plus.copy(),two.copy()).arrange(RIGHT)
		a_group.next_to(eq,LEFT)
		self.play(FadeIn(eq))
		self.play(Write(a_group))
		self.wait(3)
		#self.add(index_label(a_group))
		b_group=VGroup(two.copy(),plus.copy(),two.copy(),plus.copy(),two.copy(),plus.copy(),two.copy()).arrange(RIGHT)
		b_group.next_to(eq,LEFT)
		a=Eq(a_group)
		b=Eq(b_group)
		self.play(ReplacementTransform(a.get_slice(0,1,2,3,4),b.get_slice(0,1,2,3,4)),FadeIn(b.get_slice(5,6),shift=UP))
		self.wait(3)
		brace_1=Brace(b_group,UP)	
		brace_1_text=Tex(r"বার যোগ ",tex_template = myTemplate)
		brace_1_Group=VGroup(MathTex("4"),brace_1_text).arrange(RIGHT).next_to(brace_1,UP)
		count=MathTex("4").scale(scale)
		count_5=MathTex("5").scale(scale)
		count_group_1=VGroup(two.copy(),times.copy(),count).arrange(RIGHT).next_to(eq)
		count_group_2=VGroup(three.copy(),times.copy(),count_5).arrange(RIGHT).next_to(eq)
		self.play(FadeIn(brace_1),FadeIn(brace_1_Group,shift=LEFT))
		self.wait(2)
		c=Eq(count_group_1)
		d=Eq(brace_1_Group)
		self.play(
			TransformFromCopy(b.get_slice(0,2,4,6),c.get_slice(0,0,0,0),
			path_arc=-40*DEGREES)
			)
		self.wait()
		self.play(
			FadeIn(c.get_slice(1)),
			TransformFromCopy(d.get_slice(0),c.get_slice(2),path_arc=60*DEGREES)
			)
		self.wait(2)

		gunno=Tex(r"কোন সংখ্যাটি বার বার যোগ অবস্থায় আছে ?",tex_template=myTemplate)
		gunno.next_to(c.get_slice(0),DOWN*5)
		gunno_arrow=Arrow(gunno.get_top(),c.get_slice(0).get_bottom())
		self.play(FadeIn(gunno,shift=LEFT),GrowArrow(gunno_arrow))
		self.wait(2)
		gunok=Tex(r"কত বার যোগ অবস্থায় আছে ?",tex_template=myTemplate)
		gunok.next_to(c.get_slice(2),5*UP)
		gunok_arrow=Arrow(gunok.get_bottom(),c.get_slice(2).get_top())
		self.play(FadeIn(gunok,shift=RIGHT),GrowArrow(gunok_arrow))
		self.wait(3)

		all_objects=[gunno,gunno_arrow,gunok,gunok_arrow]
		self.play(*[FadeOut(obj,shift=RIGHT) for obj in all_objects])
		self.wait()

		############# just test
		c_group=VGroup(two.copy(),plus.copy(),two.copy(),plus.copy(),two.copy(),plus.copy(),two.copy(),plus.copy(),two.copy()).arrange(RIGHT)
		c_group.next_to(eq,LEFT)
		brace_2=Brace(c_group,UP)
		e=Eq(c_group)
		five=MathTex("5")
		five.add_updater(lambda x:x.next_to(brace_1_text,LEFT))
		self.play(ReplacementTransform(b.get_slice(0,1,2,3,4,5,6),e.get_slice(0,1,2,3,4,5,6)),
			LaggedStart(FadeIn(e.get_slice(7,8),shift=UP,lag_ratio=0.5)),
			Transform(brace_1,brace_2),
			FadeOut(brace_1_Group[0],shift=LEFT),FadeIn(five,shift=DOWN),
			brace_1_text.animate.next_to(brace_2,UP)
			)
		self.play(FadeOut(count_group_1[2],shift=DOWN),
			TransformFromCopy(five,count_group_2[2],path_arc=65*DEGREES))
		self.wait(3)

		d_group=VGroup(three.copy(),plus.copy(),three.copy(),plus.copy(),three.copy(),plus.copy(),three.copy(),plus.copy(),three.copy()).arrange(RIGHT)
		d_group.next_to(eq,LEFT)
		f=Eq(d_group)
		self.play(ReplacementTransform(e.get_slice(0,2,4,6,8),f.get_slice(0,2,4,6,8),lag_ratio=0.5,run_time=2))
		g=Eq(count_group_2)
		self.play(FadeOut(count_group_1[0],shift=UP),
			TransformFromCopy(f.get_slice(0,2,4,6,8),g.get_slice(0,0,0,0,0),path_arc=-45*DEGREES))
		self.wait(3)

		all_objectss=[five,brace_1_text,brace_1,e.get_slice(1,3,5,7),f.get_slice(0,2,4,6,8),g.get_slice(0,2),c.get_slice(1),eq]
		self.play(*[FadeOut(obj,shift=DOWN) for obj in all_objectss])
		self.wait(2)

		question=Tex(r"গুণ মানে কী? ",tex_template=myTemplate)
		ans=Tex(r"গুণ মানে একই সংখ্যা বার বার যোগ করা",tex_template=myTemplate)
		qa=VGroup(question,ans).arrange(DOWN,buff=2)
		self.play(Write(question))
		self.wait(4)
		self.play(FadeIn(ans,scale=2),run_time=2)
		self.wait(2)

class Intro2(Scene):
	def construct(self):
		ques=Tex(r"তুমি কি অনুমান করতে পারবে, বার বার বিয়োগের আইডিয়াটা কী?",tex_template=myTemplate)
		self.play(Write(ques))
		self.wait(2)


class Intro3(Scene):
	def construct(self):
		scale=1.8
		two=MathTex("2").scale(scale)
		three=MathTex("3").scale(scale)
		times=MathTex(r"\times").scale(scale)
		eq=MathTex("=").scale(scale)
		group_1=VGroup(two.copy(),times.copy(),two.copy(),times.copy(),two.copy(),times.copy(),two.copy()).arrange(RIGHT)
		group_1.next_to(eq,LEFT)
		group_2=VGroup(two.copy(),times.copy(),two.copy(),times.copy(),two.copy(),times.copy(),two.copy(),times.copy(),two.copy()).arrange(RIGHT)
		group_2.next_to(eq,LEFT)
		count_4=MathTex("4")
		count_5=MathTex("5")
		brace_1=Brace(group_1,UP)
		brace_2=Brace(group_2,UP)
		brace_text=Tex(r"বার গুণ ",tex_template=myTemplate)
		brace_texg_1=VGroup(count_4,brace_text).arrange(RIGHT)
		brace_texg_1.add_updater(lambda x:x.next_to(brace_1,UP))
		# count_5.add_updater(lambda x: x.next_to(brace_text,LEFT))
		result_1=MathTex("2^4",substrings_to_isolate=["^"]).scale(scale)
		result_1.next_to(eq,RIGHT)
		result_2=MathTex("3^5",substrings_to_isolate=["^"]).scale(scale)
		result_2.next_to(eq,RIGHT)

		self.play(Write(group_1))
		self.wait(3)
		self.play(FadeIn(brace_1),FadeIn(brace_texg_1,shift=RIGHT))
		self.wait(2)
		self.play(Write(eq))

		a=Eq(group_1)
		b=Eq(result_1)
		c=Eq(group_2)
		d=Eq(result_2)
		self.play(TransformFromCopy(a.get_slice(0,2,4,6),b.get_slice(0,0,0,0),path_arc=-45*DEGREES))
		self.wait(2)
		self.play(TransformFromCopy(brace_texg_1[0],b.get_slice(2),path_arc=60*DEGREES))
		self.wait(2)
		############

		gunno=Tex(r"কোন সংখ্যাটি বার বার গুণ অবস্থায় আছে ?",tex_template=myTemplate)
		gunno.next_to(b.get_slice(0),DOWN*5)
		gunno_arrow=Arrow(gunno.get_top(),b.get_slice(0).get_bottom())
		self.play(FadeIn(gunno,shift=LEFT),GrowArrow(gunno_arrow))
		self.wait(2)
		gunok=Tex(r"কত বার গুণ অবস্থায় আছে ?",tex_template=myTemplate)
		gunok.next_to(b.get_slice(2),5*UP)
		gunok_arrow=Arrow(gunok.get_bottom(),b.get_slice(2).get_top())
		self.play(FadeIn(gunok,shift=RIGHT),GrowArrow(gunok_arrow))
		self.wait(3)

		all_objects=[gunno,gunno_arrow,gunok,gunok_arrow]
		self.play(*[FadeOut(obj,shift=RIGHT) for obj in all_objects])
		self.wait()

		##############



		count_5.add_updater(lambda x:x.next_to(brace_text,LEFT))
		self.play(ReplacementTransform(a.get_slice(0,1,2,3,4,5,6),c.get_slice(0,1,2,3,4,5,6)),
			LaggedStart(FadeIn(c.get_slice(7,8),shift=UP,lag_ratio=0.7)),
			ReplacementTransform(brace_1,brace_2),
			brace_texg_1.animate.next_to(brace_2,UP),
			FadeOut(brace_texg_1[0],shift=UP),FadeIn(count_5,shift=DOWN),
			)
		self.play(TransformFromCopy(count_5,d.get_slice(2),path_arc=60*DEGREES),
			FadeOut(b.get_slice(2),scale=0.3))

		self.wait(2)
		group_3=VGroup(three.copy(),times.copy(),three.copy(),times.copy(),three.copy(),times.copy(),three.copy(),
			times.copy(),three.copy()).arrange(RIGHT)
		group_3.next_to(eq,LEFT)
		e=Eq(group_3)
		self.play(ReplacementTransform(c.get_slice(0,2,4,6,8),e.get_slice(0,2,4,6,8),lag_ratio=0.5))
		self.play(FadeOut(b.get_slice(0),scale=0.3),
			TransformFromCopy(e.get_slice(0,2,4,6,8),d.get_slice(0,0,0,0,0),path_arc=-45*DEGREES))
		self.wait(3)

		all_objectss=[brace_2,brace_texg_1,count_5, group_2,group_3,eq]
		self.play(*[FadeOut(obj,shift=DOWN) for obj in all_objectss])
		self.wait(2)
		self.play(result_2.animate.move_to(ORIGIN))
		# self.play(FadeOut(b.get_slice(1)),FadeOut(d.get_slice(0,2)))
		self.wait(3)


		vitti=Tex(r"ভিত্তি",tex_template=myTemplate)
		nidhan=Tex(r"নিধান",tex_template=myTemplate)
		base=Text("Base")
		base_gp=VGroup(vitti,nidhan,base).arrange(RIGHT,buff=2)
		base_gp.next_to(result_2,DOWN*5)
		arrow_gps=VGroup(*[Arrow(result_2.get_bottom(),m.get_top()) for m in base_gp])
		self.play(LaggedStart(FadeIn(base_gp,shift=UP,lag_ratio=0.5)),
			FadeIn(arrow_gps))
		self.wait(2)
		suchok=Tex(r"সূচক",tex_template=myTemplate)
		shokti=Tex(r"শক্তি",tex_template=myTemplate)
		matra=Tex(r"মাত্রা",tex_template=myTemplate)
		ghat=Tex(r"ঘাত",tex_template=myTemplate)
		kromo=Tex(r"ক্রম",tex_template=myTemplate)
		suchok_gp1=VGroup(suchok,shokti,matra,ghat,kromo).arrange(RIGHT,buff=2)
		suchok_gp1.next_to(result_2,UP*5)
		arrow_gps2=VGroup(*[Arrow(result_2[2].get_top(),m.get_bottom()) for m in suchok_gp1])
		self.play(LaggedStart(FadeIn(suchok_gp1,shift=UP,lag_ratio=0.5)),
			FadeIn(arrow_gps2))
		self.wait(2)

		indice=Tex("Indice")
		expo=Tex("Exponent")
		power=Tex("Power")
		degrre=Tex("Degree")
		order=Tex("Order")

		indice_gp=VGroup(indice,expo,power,degrre,order).arrange(RIGHT,buff=1).move_to(suchok_gp1)
		arrow_gps3=VGroup(*[Arrow(result_2[2].get_top(),m.get_bottom()) for m in indice_gp])
		self.play(FadeOut(suchok_gp1,shift=UP),FadeOut(arrow_gps2))
		self.play(LaggedStart(FadeIn(indice_gp,shift=UP,lag_ratio=0.5)),
			FadeIn(arrow_gps3))
		self.wait(3)

class Expansion(Scene):
	def construct(self):
		scale=1.8
		a=MathTex(r"5^4 = 5\times 5\times 5\times 5",substrings_to_isolate=["=","\times"] ).scale(scale)
		self.play(Write(a))
		self.wait(3)
		self.play(a.animate.move_to(UP*2))
		b=MathTex(r"(-1)^3= (-1)\times (-1)\times (-1)").scale(scale)
		self.play(Write(b))
		self.wait(3)
		self.play(FadeOut(a),b.animate.move_to(UP*2))
		c=MathTex("-1","^3","=","-","1",r"\times","1",r"\times","1").scale(scale)
		self.play(Write(c))
		# self.add(index_label(c))
		self.wait(4)
		d=MathTex("(","2^3",")",r"^2","=","2^3",r"\times","2^3").scale(scale)
		d1=Eq(d)
		self.play(FadeOut(b),c.animate.move_to(UP*2))
		self.play(FadeIn(d1.get_slice(0,1,2,3)))
		self.wait(2)
		self.play(Write(d[4]))
		self.wait(2)
		self.play(TransformFromCopy(d1.get_slice(1,1),d1.get_slice(5,7),path_arc=-55*DEGREES))
		self.play(FadeIn(d[6],shift=UP))
		self.wait(2)
		e=MathTex("(-2^3)",r"^2","=","(-2^3)",r"\times","(-2^3)").scale(scale)
		e1=Eq(e)
		self.play(FadeOut(c), d.animate.move_to(UP*2))
		self.play(Write(e1.get_slice(0,1)))
		self.wait(2)
		self.play(Write(e[2]))
		self.play(TransformFromCopy(e1.get_slice(0,0),e1.get_slice(3,5),path_arc=-60*DEGREES))
		self.play(FadeIn(e[4],shift=UP))
		self.wait(2)
		gp=VGroup(d,e)
		self.play(LaggedStart(FadeOut(gp,shift=DOWN)),lag_ratio=0.5)
		self.wait(2)













		

		











