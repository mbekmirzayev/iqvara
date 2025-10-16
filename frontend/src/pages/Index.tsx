import { Header } from "@/components/Header";
import { Hero } from "@/components/Hero";
import { Stats } from "@/components/Stats";
import { Professions } from "@/components/Professions";
import { CoursesPreview } from "@/components/CoursesPreview";
import { AllCourses } from "@/components/AllCourses";
import { BlogSection } from "@/components/BlogSection";
import { Contact } from "@/components/Contact";
import { Footer } from "@/components/Footer";

const Index = () => {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main>
        <Hero />
        <Stats />
        <Professions />
        <CoursesPreview />
        <AllCourses />
        <BlogSection />
        <Contact />
      </main>
      <Footer />
    </div>
  );
};

export default Index;
