import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Calendar, User, ArrowRight } from "lucide-react";

interface BlogCardProps {
  title: string;
  excerpt: string;
  author: string;
  date: string;
  category: string;
  image: string;
  readTime: string;
}

export const BlogCard = ({
  title,
  excerpt,
  author,
  date,
  category,
  image,
  readTime,
}: BlogCardProps) => {
  return (
    <Card className="group overflow-hidden hover:shadow-xl transition-all duration-300 hover:-translate-y-1 cursor-pointer">
      <div className="relative h-56 overflow-hidden">
        <div 
          className="absolute inset-0 bg-gradient-to-br from-primary/30 to-accent/30 group-hover:scale-110 transition-transform duration-500"
          style={{ backgroundColor: image }}
        />
        <Badge className="absolute top-4 left-4 bg-accent text-accent-foreground">
          {category}
        </Badge>
        <div className="absolute top-4 right-4 bg-white/90 text-foreground text-xs px-3 py-1 rounded-full font-medium">
          {readTime}
        </div>
      </div>
      
      <CardHeader>
        <h3 className="text-xl font-bold text-foreground line-clamp-2 group-hover:text-primary transition-colors">
          {title}
        </h3>
      </CardHeader>
      
      <CardContent>
        <p className="text-muted-foreground text-sm line-clamp-3 mb-4">
          {excerpt}
        </p>
        
        <div className="flex items-center justify-between text-xs text-muted-foreground">
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-1">
              <User className="h-3 w-3" />
              <span>{author}</span>
            </div>
            <div className="flex items-center gap-1">
              <Calendar className="h-3 w-3" />
              <span>{date}</span>
            </div>
          </div>
          <ArrowRight className="h-4 w-4 group-hover:translate-x-1 transition-transform" />
        </div>
      </CardContent>
    </Card>
  );
};
