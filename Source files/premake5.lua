local Root = os.getenv("ROOT")
local Name = os.getenv("NAME")

if not Root then
    error("Environment variable ROOT not set")
end
if not Name or Name == "" then
   error("Name doesn't exist")
end


workspace(Name)
   location(Root)
   architecture "x64"
   configurations { "Debug", "Release" }
   startproject(Name)

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

project(Name)
   location(Root .. "/build")
   kind "ConsoleApp"
   language "C++"
   cppdialect "C++20"

   targetdir (Root .. "/bin/" .. outputdir)
   objdir (Root .. "/bin-int/" .. outputdir)

   files {
      "src/**.h",
      "src/**.cpp"
   }

   includedirs {
      "include"
   }

   filter "system:windows"
      systemversion "latest"
      defines { "PLATFORM_WINDOWS" }

   filter "configurations:Debug"
      symbols "On"

   filter "configurations:Release"
      optimize "On"
