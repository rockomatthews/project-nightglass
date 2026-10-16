using UnrealBuildTool;
using System.Collections.Generic;
public class NightglassTarget : TargetRules
{
    public NightglassTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Game;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        ExtraModuleNames.Add("Nightglass");
    }
}
