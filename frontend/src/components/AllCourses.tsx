import { useState } from "react";
import { CourseCard } from "./CourseCard";
import { Button } from "@/components/ui/button";

const allCourses = [
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
    title: "Digital Marketing Strategy",
    description: "Master SEO, content marketing, and social media strategies",
    category: "Marketing",
    lessons: 35,
    rating: 4.8,
    reviews: 678,
    price: "$54.99",
    image: "hsl(160, 70%, 50%)",
    type: "certificate" as const,
    purchases: 1987,
  },
  {
    title: "Data Science with Python",
    description: "Learn data analysis, visualization, and machine learning",
    category: "Data Science",
    lessons: 48,
    rating: 4.9,
    reviews: 890,
    price: "$64.99",
    image: "hsl(200, 80%, 55%)",
    type: "certificate" as const,
    purchases: 3201,
  },
];

const categories = ["All", "Development", "Design", "Marketing", "Data Science"];

export const AllCourses = () => {
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [sortBy, setSortBy] = useState<"default" | "price-high" | "price-low" | "free">("default");
  const [isLoggedIn] = useState(false); // TODO: Connect to auth system

  let filteredCourses = selectedCategory === "All" 
    ? allCourses 
    : allCourses.filter(course => course.category === selectedCategory);

  // Apply sort filters
  if (sortBy === "free") {
    filteredCourses = filteredCourses.filter(course => course.type === "free");
  } else if (sortBy === "price-high") {
    filteredCourses = [...filteredCourses].sort((a, b) => {
      const priceA = parseFloat(a.price.replace("$", ""));
      const priceB = parseFloat(b.price.replace("$", ""));
      return priceB - priceA;
    });
  } else if (sortBy === "price-low") {
    filteredCourses = [...filteredCourses].sort((a, b) => {
      const priceA = parseFloat(a.price.replace("$", ""));
      const priceB = parseFloat(b.price.replace("$", ""));
      return priceA - priceB;
    });
  }

  return (
    <section className="py-20 bg-background">
      <div className="container mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-4xl md:text-5xl font-bold text-foreground mb-4">
            All <span className="text-primary">Courses</span>
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Explore our complete collection of expert-led courses across various categories
          </p>
        </div>

        <div className="flex flex-col sm:flex-row justify-between items-center gap-4 mb-12">
          <div className="flex flex-wrap justify-center gap-3">
            {categories.map((category) => (
              <Button
                key={category}
                variant={selectedCategory === category ? "default" : "outline"}
                onClick={() => setSelectedCategory(category)}
                className="transition-all duration-300"
              >
                {category}
              </Button>
            ))}
          </div>

          <div className="flex flex-wrap gap-2">
            <Button
              variant={sortBy === "default" ? "default" : "outline"}
              onClick={() => setSortBy("default")}
              size="sm"
            >
              Default
            </Button>
            <Button
              variant={sortBy === "price-high" ? "default" : "outline"}
              onClick={() => setSortBy("price-high")}
              size="sm"
            >
              Price: High to Low
            </Button>
            <Button
              variant={sortBy === "price-low" ? "default" : "outline"}
              onClick={() => setSortBy("price-low")}
              size="sm"
            >
              Price: Low to High
            </Button>
            <Button
              variant={sortBy === "free" ? "default" : "outline"}
              onClick={() => setSortBy("free")}
              size="sm"
            >
              Free Only
            </Button>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredCourses.map((course, index) => (
            <CourseCard 
              key={index} 
              {...course} 
              isLocked={!isLoggedIn && course.type === "certificate"}
            />
          ))}
        </div>
      </div>
    </section>
  );
};
