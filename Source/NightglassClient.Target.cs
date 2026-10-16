using UnrealBuildTool;
using System.Collections.Generic;
public class NightglassClientTarget : TargetRules
{
    public NightglassClientTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Client;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        ExtraModuleNames.Add("Nightglass");
    }
}
