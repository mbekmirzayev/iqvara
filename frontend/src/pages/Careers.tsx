import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Briefcase, MapPin, Clock } from "lucide-react";

const Careers = () => {
  const openings = [
    {
      title: "Senior Frontend Developer",
      department: "Engineering",
      location: "Remote",
      type: "Full-time",
      description: "We're looking for an experienced frontend developer to help build the future of online education."
    },
    {
      title: "Content Creator - Web Development",
      department: "Education",
      location: "Remote",
      type: "Contract",
      description: "Create engaging course content for our web development curriculum."
    },
    {
      title: "UX/UI Designer",
      department: "Design",
      location: "Remote",
      type: "Full-time",
      description: "Design beautiful and intuitive learning experiences for our students."
    },
    {
      title: "Marketing Manager",
      department: "Marketing",
      location: "Hybrid",
      type: "Full-time",
      description: "Lead our marketing efforts to reach more learners worldwide."
    }
  ];

  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main>
        <section className="py-20 bg-gradient-to-b from-primary/10 to-background">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h1 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
                Join Our <span className="text-primary">Team</span>
              </h1>
              <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
                Help us transform education and empower learners around the world
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-5xl mx-auto">
              {openings.map((job, index) => (
                <Card key={index} className="hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <div className="flex items-start justify-between mb-2">
                      <div className="flex items-center gap-2">
                        <Briefcase className="h-5 w-5 text-primary" />
                        <span className="text-sm font-medium text-primary">{job.department}</span>
                      </div>
                    </div>
                    <CardTitle className="text-xl">{job.title}</CardTitle>
                    <CardDescription>{job.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="flex items-center gap-4 text-sm text-muted-foreground mb-4">
                      <div className="flex items-center gap-1">
                        <MapPin className="h-4 w-4" />
                        <span>{job.location}</span>
                      </div>
                      <div className="flex items-center gap-1">
                        <Clock className="h-4 w-4" />
                        <span>{job.type}</span>
                      </div>
                    </div>
                    <Button variant="default" className="w-full">Apply Now</Button>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </div>
  );
};

export default Careers;
