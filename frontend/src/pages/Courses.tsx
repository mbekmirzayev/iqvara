import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { AllCourses } from "@/components/AllCourses";

const Courses = () => {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main className="pt-8">
        <AllCourses />
      </main>
      <Footer />
    </div>
  );
};

export default Courses;
