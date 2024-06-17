from fpdf import FPDF

class PDF(FPDF):

    def add_shirt_image(self, name):

        self.image("shirtificate.png", x=35, y=60, w=140)


        self.set_font("Arial", 'B', 24)
        self.set_text_color(128,0,128)
        self.cell(0, 180, f"{name} took CS50", 0, 1, 'C')

def main():

    name = input("Name: ")


    pdf = PDF()
    pdf.add_page()


    pdf.add_shirt_image(name)


    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
