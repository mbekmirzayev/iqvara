import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Star, Clock, BookOpen } from "lucide-react";

interface CourseCardProps {
  title: string;
  description: string;
  category: string;
  lessons: number;
  rating: number;
  reviews: number;
  price: string;
  image: string;
  type: "certificate" | "free";
  purchases: number;
  isLocked?: boolean;
}

export const CourseCard = ({
  title,
  description,
  category,
  lessons,
  rating,
  reviews,
  price,
  image,
  type,
  purchases,
  isLocked = false,
}: CourseCardProps) => {
  return (
    <Card className="group overflow-hidden hover:shadow-xl transition-all duration-300 hover:-translate-y-1 cursor-pointer relative">
      <div className="relative h-48 overflow-hidden">
        <div 
          className="absolute inset-0 bg-gradient-to-br from-primary/20 to-accent/20 group-hover:scale-110 transition-transform duration-500"
          style={{ backgroundColor: image }}
        />
        {isLocked && (
          <div className="absolute inset-0 bg-black/60 flex items-center justify-center backdrop-blur-sm z-10">
            <div className="text-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-white mx-auto mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              <p className="text-white font-semibold">Login to access</p>
            </div>
          </div>
        )}
        <Badge className="absolute top-4 left-4 bg-accent text-accent-foreground z-20">
          {category}
        </Badge>
        <Badge className="absolute top-4 right-4 bg-primary text-primary-foreground z-20">
          {type === "free" ? "Free" : "Certificate"}
        </Badge>
      </div>
      
      <CardHeader>
        <h3 className="text-xl font-bold text-foreground line-clamp-2 group-hover:text-primary transition-colors">
          {title}
        </h3>
      </CardHeader>
      
      <CardContent>
        <p className="text-muted-foreground text-sm line-clamp-2 mb-4">
          {description}
        </p>
        
        <div className="flex items-center gap-4 text-sm text-muted-foreground flex-wrap">
          <div className="flex items-center gap-1">
            <BookOpen className="h-4 w-4" />
            <span>{lessons} lessons</span>
          </div>
          <div className="flex items-center gap-1">
            <Star className="h-4 w-4 fill-accent text-accent" />
            <span>{rating} ({reviews})</span>
          </div>
          <div className="flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
            <span>{purchases} enrolled</span>
          </div>
        </div>
      </CardContent>
      
      <CardFooter className="flex items-center justify-between">
        <div className="text-2xl font-bold text-primary">{type === "free" ? "Free" : price}</div>
        <Button variant="default" size="sm" disabled={isLocked}>
          {isLocked ? "Login Required" : "Enroll Now"}
        </Button>
      </CardFooter>
    </Card>
  );
};
