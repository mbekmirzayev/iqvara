import { Button } from "@/components/ui/button";
import heroImage from "@/assets/hero-learning.jpg";
import { ArrowRight } from "lucide-react";

export const Hero = () => {
  return (
    <section className="relative overflow-hidden">
      <div 
        className="absolute inset-0 bg-cover bg-center"
        style={{ backgroundImage: `url(${heroImage})` }}
      >
        <div className="absolute inset-0 bg-gradient-to-r from-primary/90 via-primary/80 to-accent/70" />
      </div>
      
      <div className="relative container mx-auto px-4 py-24 md:py-32">
        <div className="max-w-3xl">
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-6 animate-in fade-in slide-in-from-bottom-4 duration-1000">
            Transform Your Future with{" "}
            <span className="text-accent">Expert Learning</span>
          </h1>
          <p className="text-xl md:text-2xl text-white/90 mb-8 animate-in fade-in slide-in-from-bottom-4 duration-1000 delay-150">
            Master in-demand skills from industry professionals. Start your journey to success today.
          </p>
          <div className="flex flex-wrap gap-4 animate-in fade-in slide-in-from-bottom-4 duration-1000 delay-300">
            <Button variant="hero" size="lg">
              Explore Courses <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
            <Button variant="outline" size="lg" className="bg-white/10 text-white border-white/30 hover:bg-white/20">
              Learn More
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};
