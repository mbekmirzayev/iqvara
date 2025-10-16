import { Users, BookOpen, Award, Globe } from "lucide-react";

const stats = [
  { icon: Users, label: "Active Students", value: "50,000+", color: "text-primary" },
  { icon: BookOpen, label: "Total Courses", value: "500+", color: "text-accent" },
  { icon: Award, label: "Certifications", value: "25,000+", color: "text-primary" },
  { icon: Globe, label: "Countries", value: "120+", color: "text-accent" },
];

export const Stats = () => {
  return (
    <section className="py-16 bg-gradient-to-b from-background to-secondary/20">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
          {stats.map((stat, index) => (
            <div 
              key={index}
              className="text-center p-6 rounded-xl bg-card hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
            >
              <stat.icon className={`h-12 w-12 mx-auto mb-4 ${stat.color}`} />
              <div className="text-3xl md:text-4xl font-bold text-foreground mb-2">
                {stat.value}
              </div>
              <div className="text-sm text-muted-foreground font-medium">
                {stat.label}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
