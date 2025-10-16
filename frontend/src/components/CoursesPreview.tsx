import { CourseCard } from "./CourseCard";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

const categories = [
  {
    name: "Web Development",
    courses: [
      {
        title: "Complete React & TypeScript Masterclass",
        description: "Master modern web development with React, TypeScript, and best practices",
        category: "Development",
        lessons: 42,
        rating: 4.8,
        reviews: 1234,
        price: "$49.99",
        image: "hsl(262, 52%, 47%)",
        type: "certificate" as const,
        purchases: 3456,
      },
      {
        title: "Full Stack JavaScript Development",
        description: "Build complete web applications from frontend to backend",
        category: "Development",
        lessons: 56,
        rating: 4.9,
        reviews: 987,
        price: "$59.99",
        image: "hsl(220, 70%, 55%)",
        type: "certificate" as const,
        purchases: 2890,
      },
      {
        title: "Modern CSS & Tailwind CSS",
        description: "Create beautiful, responsive designs with modern CSS techniques",
        category: "Development",
        lessons: 28,
        rating: 4.7,
        reviews: 765,
        price: "$39.99",
        image: "hsl(20, 100%, 60%)",
        type: "free" as const,
        purchases: 5678,
      },
      {
        title: "Advanced Node.js & Express",
        description: "Build scalable backend applications with Node.js and Express",
        category: "Development",
        lessons: 38,
        rating: 4.8,
        reviews: 654,
        price: "$54.99",
        image: "hsl(262, 52%, 60%)",
        type: "certificate" as const,
        purchases: 1987,
      },
    ],
  },
  {
    name: "Design",
    courses: [
      {
        title: "UI/UX Design Fundamentals",
        description: "Learn the principles of creating beautiful user interfaces",
        category: "Design",
        lessons: 32,
        rating: 4.9,
        reviews: 543,
        price: "$44.99",
        image: "hsl(280, 60%, 55%)",
        type: "certificate" as const,
        purchases: 2134,
      },
      {
        title: "Figma for Beginners",
        description: "Master the most popular design tool for UI/UX designers",
        category: "Design",
        lessons: 24,
        rating: 4.7,
        reviews: 432,
        price: "$34.99",
        image: "hsl(340, 80%, 60%)",
        type: "free" as const,
        purchases: 4321,
      },
      {
        title: "Advanced Prototyping Techniques",
        description: "Create interactive prototypes that bring your designs to life",
        category: "Design",
        lessons: 20,
        rating: 4.8,
        reviews: 321,
        price: "$39.99",
        image: "hsl(180, 60%, 50%)",
        type: "certificate" as const,
        purchases: 1654,
      },
      {
        title: "Design Systems Mastery",
        description: "Build scalable design systems for modern applications",
        category: "Design",
        lessons: 26,
        rating: 4.9,
        reviews: 298,
        price: "$49.99",
        image: "hsl(140, 70%, 50%)",
        type: "certificate" as const,
        purchases: 1876,
      },
    ],
  },
];

export const CoursesPreview = () => {
  return (
    <section className="py-20 bg-gradient-to-b from-secondary/20 to-background">
      <div className="container mx-auto px-4">
        {categories.map((category, categoryIndex) => (
          <div key={categoryIndex} className="mb-16 last:mb-0">
            <div className="flex items-center justify-between mb-8">
              <h2 className="text-3xl md:text-4xl font-bold text-foreground">
                {category.name} <span className="text-primary">Courses</span>
              </h2>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
              {category.courses.map((course, courseIndex) => (
                <CourseCard key={courseIndex} {...course} />
              ))}
            </div>

            <div className="text-center">
              <Button variant="outline" size="lg">
                View All {category.name} Courses <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};
