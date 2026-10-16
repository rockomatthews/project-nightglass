using UnrealBuildTool;
using System.Collections.Generic;
public class NightglassServerTarget : TargetRules
{
    public NightglassServerTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Server;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        ExtraModuleNames.Add("Nightglass");
    }
}
