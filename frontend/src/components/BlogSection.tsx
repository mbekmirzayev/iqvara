import { BlogCard } from "./BlogCard";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

const blogs = [
  {
    title: "10 Essential Web Development Skills for 2025",
    excerpt: "Discover the most in-demand skills every web developer should master to stay competitive in the evolving tech landscape.",
    author: "Sarah Johnson",
    date: "Jan 15, 2025",
    category: "Development",
    image: "hsl(262, 52%, 47%)",
    readTime: "5 min read",
  },
  {
    title: "The Future of UI/UX Design: Trends to Watch",
    excerpt: "Explore emerging design trends and how they're shaping the future of user experience in digital products.",
    author: "Michael Chen",
    date: "Jan 12, 2025",
    category: "Design",
    image: "hsl(280, 60%, 55%)",
    readTime: "7 min read",
  },
  {
    title: "Mastering Digital Marketing in the AI Era",
    excerpt: "Learn how artificial intelligence is revolutionizing digital marketing strategies and what it means for marketers.",
    author: "Emily Rodriguez",
    date: "Jan 10, 2025",
    category: "Marketing",
    image: "hsl(20, 100%, 60%)",
    readTime: "6 min read",
  },
];

export const BlogSection = () => {
  return (
    <section className="py-20 bg-gradient-to-b from-background to-secondary/20">
      <div className="container mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
            Latest from Our <span className="text-primary">Blog</span>
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Insights, tips, and industry trends from our expert instructors and community
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {blogs.map((blog, index) => (
            <BlogCard key={index} {...blog} />
          ))}
        </div>

        <div className="text-center">
          <Button variant="outline" size="lg">
            View All Blog Posts <ArrowRight className="ml-2 h-5 w-5" />
          </Button>
        </div>
      </div>
    </section>
  );
};
