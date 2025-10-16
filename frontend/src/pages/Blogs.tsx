import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { BlogSection } from "@/components/BlogSection";

const Blogs = () => {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      <main className="pt-8">
        <div className="container mx-auto px-4 py-12">
          <div className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
              Our <span className="text-primary">Blog</span>
            </h1>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Insights, tutorials, and industry trends from our experts
            </p>
          </div>
        </div>
        <BlogSection />
      </main>
      <Footer />
    </div>
  );
};

export default Blogs;
