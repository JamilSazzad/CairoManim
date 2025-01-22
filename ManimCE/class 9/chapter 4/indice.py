
from manim import *
import numpy as np

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
class Eq2(VGroup):
    def __init__(self, tex,**kwargs):
        self.formula=tex
    def get_slice(self):
        return VGroup(*[self.formula[i] for i in range(len(self.formula[0]))])

class BaseExponent(Scene):
	# def construct(self):
	# 	pass
	def get_all_braces(self,series,partial_sums,group,skip,scale=1):
		all_braces=[VGroup(Brace(series[:n]).set_color(BLUE)) for n in range(group,len(series)+1,skip)]
		for brace,bracetex in zip(all_braces,partial_sums):
			number=MathTex(r'''%s'''%bracetex).scale(scale)
			number.set_color(YELLOW)
			number.next_to(brace,DOWN)
			brace.add(number)
		return all_braces


	def expansion_x(self,nidhan,index=1):
		if index== 1:
			a=MathTex(r'''%s^1 = %s '''%(nidhan,nidhan))
		elif index==2:
			a=MathTex(r'''%s^2 = %s \times %s'''%(nidhan,nidhan,nidhan))
		elif index == 3:
			a=MathTex(r'''%s^3 = %s \times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan))
		elif index==4:
			a=MathTex(r'''%s^4 = %s \times %s \times %s \times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 5:
			a=MathTex(r'''%s^5 = %s \times %s \times %s\times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 6:
			a=MathTex(r'''%s^6 = %s \times %s \times %s\times %s \times %s\times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0]

	def p_expansion_x(self,nidhan,index=1):
		if index== 1:
			a=MathTex(r'''%s^1 = %s '''%(nidhan,nidhan))
		elif index==2:
			a=MathTex(r'''\left(%s\right)^2 = %s \times %s'''%(nidhan,nidhan,nidhan))
		elif index == 3:
			a=MathTex(r'''\left(%s\right)^3 = %s \times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan))
		elif index==4:
			a=MathTex(r'''\left(%s\right)^4 = %s \times %s \times %s \times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 5:
			a=MathTex(r'''\left(%s\right)^5 = %s \times %s \times %s\times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 6:
			a=MathTex(r'''\left(%s\right)^6 = %s \times %s \times %s\times %s \times %s\times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0]


	def expansion_xny(self,nidhan,index=2,hor=1):
		if index==1:
			a=MathTex(r''' {%s \over %s} = {%s \over %s}'''%(nidhan,hor,nidhan,hor))
		elif index==2:
			a=MathTex(r'''{%s^2\over %s} = {{%s\times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,hor))
		elif index == 3:
			a=MathTex(r'''{%s^3\over %s} = {{%s\times %s \times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,hor))
		elif index==4:
			a=MathTex(r'''{%s^4\over %s} = {{%s\times %s \times %s\times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,nidhan,hor))
		elif index == 5:
			a=MathTex(r'''{%s^5\over %s} = {{%s\times %s \times %s \times %s \times%s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,nidhan,nidhan,hor))
		elif index == 6:
			a=MathTex(r'''{%s^6\over %s} = {{%s\times %s \times %s \times %s \times%s\times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan,hor))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0] 



	def expansion_xyn(self,nidhan,index=2,lob=1):
		if index==1:
			a=MathTex(r''' {%s \over %s} = {%s \over %s}'''%(lob,nidhan,lob,nidhan))
		elif index==2:
			a=MathTex(r'''{%s\over %s^2} = {%s \over {%s\times %s}}'''%(lob,nidhan,lob,nidhan,nidhan))
		elif index == 3:
			a=MathTex(r'''{%s\over %s^3} = {%s \over {%s\times %s \times %s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan))
		elif index==4:
			a=MathTex(r'''{%s\over %s^4} = {%s \over {%s\times %s \times %s\times %s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan,nidhan))
		elif index == 5:
			a=MathTex(r'''{%s\over %s^5} = {%s \over {%s\times %s \times %s \times %s \times%s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 6:
			a=MathTex(r'''{%s\over %s^6} = {%s \over {%s\times %s \times %s \times %s \times%s\times %s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0] 

######################## negetive constant expansion 
	def f_expansion_x(self,nidhan,index=1):
		if index== 1:
			a=MathTex(r'''%s^1 = %s '''%(nidhan,nidhan))
		elif index==2:
			a=MathTex(r'''\left(%s\right)^2 = %s \times %s'''%(nidhan,nidhan,nidhan))
		elif index == 3:
			a=MathTex(r'''\left(%s\right)^3 = %s \times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan))
		elif index==4:
			a=MathTex(r'''\left(%s\right)^4 = %s \times %s \times %s \times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 5:
			a=MathTex(r'''\left(%s\right)^5 = %s \times %s \times %s\times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 6:
			a=MathTex(r'''\left(%s\right)^6 = %s \times %s \times %s\times %s \times %s\times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0]


	def nexpansion_x(self,nidhan,index=1):
		if index== 1:
			a=MathTex(r'''-%s^1 = -%s '''%(nidhan,nidhan))
		elif index==2:
			a=MathTex(r'''-%s^2 = -%s \times %s'''%(nidhan,nidhan,nidhan))
		elif index == 3:
			a=MathTex(r'''-%s^3 = -%s \times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan))
		elif index==4:
			a=MathTex(r'''-%s^4 = -%s \times %s \times %s \times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 5:
			a=MathTex(r'''-%s^5 = -%s \times %s \times %s\times %s \times %s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 6:
			a=MathTex(r'''-%s^6 = -%s \times %s \times %s\times %s \times %s\times%s'''%(nidhan,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0] 


	def nexpansion_xny(self,nidhan,index=2,hor=1):
		if index==1:
			a=MathTex(r''' {-%s \over %s} = {-%s \over %s}'''%(nidhan,hor,nidhan,hor))
		elif index==2:
			a=MathTex(r'''{-%s^2\over %s} = {-{%s\times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,hor))
		elif index == 3:
			a=MathTex(r'''{-%s^3\over %s} = {-{%s\times %s \times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,hor))
		elif index==4:
			a=MathTex(r'''{-%s^4\over %s} = {-{%s\times %s \times %s\times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,nidhan,hor))
		elif index == 5:
			a=MathTex(r'''{-%s^5\over %s} = {-{%s\times %s \times %s \times %s \times%s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,nidhan,nidhan,hor))
		elif index == 6:
			a=MathTex(r'''{-%s^6\over %s} = {-{%s\times %s \times %s \times %s \times%s\times %s}\over %s}'''%(nidhan,hor,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan,hor))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0] 



	def nexpansion_xyn(self,nidhan,index=2,lob=1):
		if index==1:
			a=MathTex(r''' {%s \over -%s} = {%s \over -%s}'''%(lob,nidhan,lob,nidhan))
		elif index==2:
			a=MathTex(r'''{%s\over -%s^2} = {%s \over -{%s\times %s}}'''%(lob,nidhan,lob,nidhan,nidhan))
		elif index == 3:
			a=MathTex(r'''{%s\over -%s^3} = {%s \over -{%s\times %s \times %s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan))
		elif index==4:
			a=MathTex(r'''{%s\over -%s^4} = {%s \over -{%s\times %s \times %s\times %s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan,nidhan))
		elif index == 5:
			a=MathTex(r'''{%s\over -%s^5} = {%s \over -{%s\times %s \times %s \times %s \times%s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan,nidhan,nidhan))
		elif index == 6:
			a=MathTex(r'''{%s\over -%s^6} = {%s \over -{%s\times %s \times %s \times %s \times%s\times %s}}'''%(lob,nidhan,lob,nidhan,nidhan,nidhan,nidhan,nidhan,nidhan))
		else:
			a=Text("Sorry, index should be 6 or less")

		return a[0] 


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

class Expansion(BaseExponent):
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
#####################################################
		self.expansion_mul1()
		self.wait(2)




## animation method

	def expansion_3(self):
		m=self.expansion_x(r"\left(-{2\over 3}\right)",index=4)
		# m1=Eq(m[0])
		n=self.nexpansion_xyn(r"(a+b)",index=3,lob="y")
		self.play(Write(n))
		# self.add(index_label(n[0]))
		self.wait(2)

	def expansion_mul1(self):
		two=self.f_expansion_x(r"{1 \over 3}",5).scale(2).to_edge(LEFT)
		series=two[8:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"{1 \over 2}",r"{1 \over 4}",r"{1 \over 8}",r"{1 \over 16}",r"{1 \over 32}"]
		braces=self.get_all_braces(series,partial_sums,2,4,2)
		brace=braces[0]
		self.add(two,brace)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
	

class Skill_1(BaseExponent):
	def construct(self):
		# self.scale=2
		# two=self.expansion_x("2",4).scale(self.scale)
		# five=self.expansion_x("5",7).scale(scale)
		# one=self.expansion_x("1",5).scale(scale)
		# half=self.f_expansion_x(r"{1 \over 2}",4).scale(scale)
		# four_seven=self.f_expansion_x(r"{7 \over 4}",5).scale(scale)
		# # two=self.expansion_x("2",3).scale(scale)
		# self.play(Write(two),run_time=2)
		self.expansion_mul2()
		self.expansion_mul5()
		self.expansion_mul1()
		self.expansion_mulhalf()
		self.expansion_mul7_4()

		self.neg_expansion_mul2()
		self.neg_expansion_mul1()
		self.neg_expansion_mul5()
		self.neg_expansion_mulhalf()
		self.neg_expansion_mul7_4()

		self.multipower2()
		self.multipower3()
		self.multipower_n2()
		self.multipower_n3()
		self.wait()

	def expansion_mul2(self):
		two=self.expansion_x(r"2",4).scale(2)
		two_group=Eq(two)
		self.play(Write(two[:3]))
		self.wait(2)
		self.play(TransformFromCopy(two_group.get_slice(0,0,0,0),two_group.get_slice(3,5,7,9),path_arc=-45*DEGREES),
			LaggedStart(FadeIn(two_group.get_slice(4,6,8),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=two[3:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"2^1",r"2^2",r"2^3",r"2^4"]
		braces=self.get_all_braces(series,partial_sums,1,2,2)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(two))

	def neg_expansion_mul2(self):
		two=self.expansion_x(r"(-2)",4).scale(1.5)
		two_group=Eq(two)
		a,b,c,d,e=two[:4],two[6:10],two[11:15],two[16:20],two[21:25]
		two_vgroup=VGroup(a,b,c,d,e)
		t=Eq(two_vgroup)
		self.play(Write(two[:6]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0,0),t.get_slice(1,2,3,4),path_arc=-45*DEGREES),
			LaggedStart(FadeIn(two_group.get_slice(10,15,20),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=two_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"(-2)^1",r"(-2)^2",r"(-2)^3",r"(-2)^4"]
		braces=self.get_all_braces(series,partial_sums,1,1,1.5)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(two))
	def expansion_mul5(self):
		five=self.expansion_x(r"5",4).scale(2)
		five_group=Eq(five)
		self.play(Write(five[:3]))
		self.wait(2)
		self.play(TransformFromCopy(five_group.get_slice(0,0,0,0),five_group.get_slice(3,5,7,9),path_arc=-45*DEGREES),
			LaggedStart(FadeIn(five_group.get_slice(4,6,8),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=five[3:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"5^1",r"5^2",r"5^3",r"5^4"]
		braces=self.get_all_braces(series,partial_sums,1,2,2)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(five))
		self.wait()	
	def expansion_mul1(self):
		five=self.expansion_x(r"1",5).scale(2)
		five_group=Eq(five)
		self.play(Write(five[:3]))
		self.wait(2)
		self.play(TransformFromCopy(five_group.get_slice(0,0,0,0,0),five_group.get_slice(3,5,7,9,11),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(five_group.get_slice(4,6,8,10),shift=UP,lag_ratio=0.4,run_time=1))
			)
		self.wait(2)
		series=five[3:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"1^1",r"1^2",r"1^3",r"1^4",r"1^5"]
		braces=self.get_all_braces(series,partial_sums,1,2,2)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(five))
		self.wait()
	def expansion_mulhalf(self):
		five=self.f_expansion_x(r"{1\over 2}",4).scale(2).shift(UP)
		five_group=Eq(five)
		self.play(Write(five[:7]))
		# self.add(index_label(five))
		self.wait(2)
		self.play(TransformFromCopy(five_group.get_slice(1,2,3,1,2,3,1,2,3,1,2,3),five_group.get_slice(7,8,9,11,12,13,15,16,17,19,20,21),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(five_group.get_slice(10,14,18),shift=UP,lag_ratio=0.4,run_time=1))
			)
		self.wait(2)
		series=five[7:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left({1 \over 2}\right)^1",r"\left({1 \over 2}\right)^2",r"\left({1 \over 2}\right)^3",r"\left({1 \over 2}\right)^4"]
		braces=self.get_all_braces(series,partial_sums,3,4,2)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(five))
	def expansion_mul7_4(self):
		five=self.f_expansion_x(r"{7\over 4}",5).scale(2).shift(UP)
		five_group=Eq(five)
		self.play(Write(five[:7]))
		# self.add(index_label(five))
		self.wait(2)
		self.play(TransformFromCopy(five_group.get_slice(1,2,3,1,2,3,1,2,3,1,2,3,1,2,3),five_group.get_slice(7,8,9,11,12,13,15,16,17,19,20,21,23,24,25),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(five_group.get_slice(10,14,18,22),shift=UP,lag_ratio=0.4,run_time=1))
			)
		self.wait(2)
		series=five[7:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left({7 \over 4}\right)^1",r"\left({7 \over 4}\right)^2",r"\left({7 \over 4}\right)^3",r"\left({7 \over 4}\right)^4",r"\left({7 \over 4}\right)^5"]
		braces=self.get_all_braces(series,partial_sums,3,4,2)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()

		self.play(FadeOut(brace),Unwrite(five))

	def neg_expansion_mul1(self):
		two=self.expansion_x(r"(-1)",5).scale(1.5)
		two_group=Eq(two)
		a,b,c,d,e,f=two[:4],two[6:10],two[11:15],two[16:20],two[21:25],two[26:30]
		two_vgroup=VGroup(a,b,c,d,e,f)
		t=Eq(two_vgroup)
		self.play(Write(two[:6]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0,0,0),t.get_slice(1,2,3,4,5),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(two_group.get_slice(10,15,20,25),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=two_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"(-1)^1",r"(-1)^2",r"(-1)^3",r"(-1)^4",r"(-1)^5"]
		braces=self.get_all_braces(series,partial_sums,1,1,1.5)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(two))

	def neg_expansion_mul5(self):
		two=self.expansion_x(r"(-5)",5).scale(1.5)
		two_group=Eq(two)
		a,b,c,d,e,f=two[:4],two[6:10],two[11:15],two[16:20],two[21:25],two[26:30]
		two_vgroup=VGroup(a,b,c,d,e,f)
		t=Eq(two_vgroup)
		self.play(Write(two[:6]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0,0,0),t.get_slice(1,2,3,4,5),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(two_group.get_slice(10,15,20,25),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=two_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"(-5)^1",r"(-5)^2",r"(-5)^3",r"(-5)^4",r"(-5)^5"]
		braces=self.get_all_braces(series,partial_sums,1,1,1.5)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(two))

	def neg_expansion_mulhalf(self):
		two=self.expansion_x(r"\left(-{1 \over 2}\right)",6).shift(UP)
		two_group=Eq(two)
		a,b,c,d,e,f,g=two[:6],two[8:14],two[15:21],two[22:28],two[29:35],two[36:42],two[43:49]
		two_vgroup=VGroup(a,b,c,d,e,f,g)
		t=Eq(two_vgroup)
		self.play(Write(two[:8]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0,0,0,0),t.get_slice(1,2,3,4,5,6),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(two_group.get_slice(14,21,28,35,42),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=two_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left(-{1 \over 2}\right)^1",r"\left(-{1 \over 2}\right)^2",r"\left(-{1 \over 2}\right)^3",r"\left(-{1 \over 2}\right)^4",r"\left(-{1 \over 2}\right)^5",r"\left(-{1 \over 2}\right)^6"]
		braces=self.get_all_braces(series,partial_sums,1,1)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(two))

	def neg_expansion_mul7_4(self):
		two=self.expansion_x(r"\left(-{7 \over 4}\right)",5).shift(UP)
		two_group=Eq(two)
		a,b,c,d,e,f=two[:6],two[8:14],two[15:21],two[22:28],two[29:35],two[36:42]
		two_vgroup=VGroup(a,b,c,d,e,f)
		t=Eq(two_vgroup)
		self.play(Write(two[:8]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0,0,0),t.get_slice(1,2,3,4,5),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(two_group.get_slice(14,21,28,35),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=two_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left(-{7 \over 4}\right)^1",r"\left(-{7 \over 4}\right)^2",r"\left(-{7 \over 4}\right)^3",r"\left(-{7 \over 4}\right)^4",r"\left(-{7 \over 4}\right)^5"]
		braces=self.get_all_braces(series,partial_sums,1,1)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(two))

	def multipower2(self):
		base=self.p_expansion_x(r"2^3",3).scale(2)
		base_group=Eq(base)
		a,b,c,d=base[1:3],base[6:8],base[9:11],base[12:14]
		base_vgroup=VGroup(a,b,c,d)
		t=Eq(base_vgroup)
		self.play(Write(base[:6]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0),t.get_slice(1,2,3),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(base_group.get_slice(8,11),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=base_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left(2^3 \right)^1",r"\left(2^3\right)^2",r"\left(2^3\right)^3"]
		braces=self.get_all_braces(series,partial_sums,1,1,2)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(base))


	def multipower_n2(self):
		base=self.expansion_x(r"\left(-2^3\right)",3).scale(1.5)
		base_group=Eq(base)
		a,b,c,d=base[:5],base[7:12],base[13:18],base[19:24]
		base_vgroup=VGroup(a,b,c,d)
		t=Eq(base_vgroup)
		self.play(Write(base[:7]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0),t.get_slice(1,2,3),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(base_group.get_slice(12,18),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=base_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left(-2^3 \right)^1",r"\left(-2^3\right)^2",r"\left(-2^3\right)^3"]
		braces=self.get_all_braces(series,partial_sums,1,1,1.5)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(base))



	def multipower3(self):
		base=self.p_expansion_x(r"3^4",5).scale(2)
		base_group=Eq(base)
		a,b,c,d,e,f=base[1:3],base[6:8],base[9:11],base[12:14],base[15:17],base[18:20]
		base_vgroup=VGroup(a,b,c,d,e,f)
		t=Eq(base_vgroup)
		self.play(Write(base[:6]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0,0,0),t.get_slice(1,2,3,4,5),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(base_group.get_slice(8,11,14,17),shift=UP,lag_ratio=0.4,run_time=2))
			)
		self.wait(2)
		series=base_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left(3^4 \right)^1",r"\left(3^4\right)^2",r"\left(3^4\right)^3",r"\left(3^4\right)^4",r"\left(3^4\right)^5"]
		braces=self.get_all_braces(series,partial_sums,1,1,2)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(base))


	def multipower_n3(self):
		base=self.expansion_x(r"\left(-3^4\right)",5)
		base_group=Eq(base)
		a,b,c,d,e,f=base[:5],base[7:12],base[13:18],base[19:24],base[25:30],base[31:36]
		base_vgroup=VGroup(a,b,c,d,e,f)
		t=Eq(base_vgroup)
		self.play(Write(base[:7]))
		self.wait(2)
		self.play(TransformFromCopy(t.get_slice(0,0,0,0,0),t.get_slice(1,2,3,4,5),path_arc=-60*DEGREES),
			LaggedStart(FadeIn(base_group.get_slice(12,18,24,30),shift=UP,lag_ratio=0.5,run_time=2))
			)
		self.wait(2)
		series=base_vgroup[1:]
		# series_num=[-3 for n in range(1,6)]
		# partial_sums=np.cumprod(series_num)
		partial_sums=[r"\left(-3^4 \right)^1",r"\left(-3^4\right)^2",r"\left(-3^4\right)^3",r"\left(-3^4\right)^4",r"\left(-3^4\right)^5"]
		braces=self.get_all_braces(series,partial_sums,1,1)
		brace=braces[0]
		self.play(FadeIn(brace))
		self.wait(2)
		for i ,new_brace in enumerate(braces[1:]):
			self.play(Transform(brace,new_brace))
			self.wait()
		self.play(FadeOut(brace),Unwrite(base))




class SomeIndex11(BaseExponent):
	def construct(self):
		a=self.expansion_x(r"\left(-3^4\right)",5)
		self.add(a)
		self.add(index_label(a))
		# two=self.expansion_x(r"(-2)",4)
		# a,b,c,d,e=two[:4],two[6:10],two[11:15],two[16:20],two[21:25]
		# two_vgroup=VGroup(a,b,c,d,e)
		# t=Eq(two_vgroup)
		# self.add(two_vgroup)
		# self.add(index_label(two_vgroup))

