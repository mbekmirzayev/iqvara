import { Code, Palette, TrendingUp, Camera, Megaphone, Database } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

const professions = [
  {
    icon: Code,
    title: "Web Development",
    description: "Build modern, responsive websites and applications",
  },
  {
    icon: Palette,
    title: "UI/UX Design",
    description: "Create beautiful and intuitive user experiences",
  },
  {
    icon: TrendingUp,
    title: "Digital Marketing",
    description: "Master SEO, social media, and content strategies",
  },
  {
    icon: Camera,
    title: "Photography",
    description: "Capture and edit stunning visual stories",
  },
  {
    icon: Megaphone,
    title: "Content Creation",
    description: "Produce engaging content across platforms",
  },
  {
    icon: Database,
    title: "Data Science",
    description: "Analyze data and build predictive models",
  },
];

export const Professions = () => {
  return (
    <section className="py-20 bg-background">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
            Skills That Shape Your <span className="text-primary">Career</span>
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            From creative fields to technical expertise, master the skills that employers are looking for
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {professions.map((profession, index) => (
            <Card 
              key={index}
              className="group hover:shadow-xl transition-all duration-300 hover:-translate-y-2 cursor-pointer border-2 hover:border-primary"
            >
              <CardContent className="p-8">
                <profession.icon className="h-12 w-12 text-primary mb-4 group-hover:scale-110 transition-transform duration-300" />
                <h3 className="text-xl font-bold text-foreground mb-2">
                  {profession.title}
                </h3>
                <p className="text-muted-foreground">
                  {profession.description}
                </p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};
