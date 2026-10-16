using UnrealBuildTool;
using System.Collections.Generic;
public class NightglassEditorTarget : TargetRules
{
    public NightglassEditorTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Editor;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        ExtraModuleNames.Add("Nightglass");
    }
}
