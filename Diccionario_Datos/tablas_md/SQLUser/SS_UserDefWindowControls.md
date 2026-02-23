# SQLUser.SS_UserDefWindowControls

**Schema:** SQLUser
**Columnas:** 54
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CON_ParREf | bigint | PK |  | NO | SS_UserDefWindow Parent Reference |
| CON_AdminAccessRequired | varchar |  |  | SI | Requires security group Administrator Access to ed... |
| CON_AlwaysDisplayItemIfBlank | varchar |  |  | SI | Always Display Item if blank |
| CON_Calculation | varchar |  |  | SI | Calculation |
| CON_Childsub | double |  |  | NO | Childsub |
| CON_ClincalPathwayText | varchar |  |  | SI | ClincalPathwayText |
| CON_Code | varchar |  |  | SI | Code |
| CON_CodeTable | varchar |  |  | SI | Code Table |
| CON_ComboScores | varchar |  |  | SI | ComboScores |
| CON_ControlGroupCode | varchar |  |  | SI | Control Group Code |
| CON_ControlGroupField | varchar |  |  | SI | Control Group Field |
| CON_ControlGroupMainControl | varchar |  |  | SI | Control Group Main Control |
| CON_ControlGroupType | varchar |  |  | SI | Control Group Type |
| CON_ControlGroupValue | varchar |  |  | SI | Control Group Value |
| CON_ControlGroupValueExtra | varchar |  |  | SI | Control Group Value Extra |
| CON_ControlType | varchar |  |  | SI | ControlType |
| CON_CreateDate | date |  |  | SI | Date Control was added to questionnaire
Only for ... |
| CON_CreateTime | time |  |  | SI | Time Control was added to questionnaire
Only for ... |
| CON_CustomType | varchar |  |  | SI | CustomType |
| CON_DBField | varchar |  |  | SI | Database Field |
| CON_DateFrom | date |  |  | SI | Date From |
| CON_DateTo | date |  |  | SI | Date To |
| CON_DaysOffsetForDefOfLastAns | double |  |  | SI | Days Offset For Default Of Last Answer |
| CON_DecPlaces | varchar |  |  | SI | Decimal Places |
| CON_DeepSee | varchar |  |  | SI | Only for Tabular Items Controls : Use to create an... |
| CON_DeepSeeExpression | varchar |  |  | SI | DeepSeeExpression |
| CON_DefaultLastQnAns | varchar |  |  | SI | Default Last Question and Answer |
| CON_Deprecated | varchar |  |  | SI | Deprecated |
| CON_DisplayAnswer | varchar |  |  | SI | DisplayAnswer |
| CON_DisplayCumulView | varchar |  |  | SI | Display question and responses in cumulutive view |
| CON_DisplayDesc | varchar |  |  | SI | DisplayDesc |
| CON_DisplayOnly | varchar |  |  | SI | DisplayOnly |
| CON_Generated | varchar |  |  | SI | Generated |
| CON_Image_DR | bigint |  | FK | SI | Des Ref Image |
| CON_IsPassword | varchar |  |  | SI | Indicate if textbox files corresponds to a passwor... |
| CON_LabelHeadingStyle | varchar |  |  | SI | LabelHeadingStyle |
| CON_LookupJSFunction | varchar |  |  | SI | LookupJSFunction |
| CON_MaxValue | double |  |  | SI | MaxValue |
| CON_MinValue | double |  |  | SI | MinValue |
| CON_NestedObsGroup_DR | bigint |  | FK | SI | Observation Group
for Nested Entry |
| CON_NoLongerUsedFlag | varchar |  |  | SI | [DEPRECATED]Functionality replaced by DateFrom and... |
| CON_ObsItem_DR | bigint |  | FK | SI | Des Ref ObsItem |
| CON_QPropName | varchar |  |  | SI | Field storing the corresponding property name in q... |
| CON_QuestionAnswerLink | varchar |  |  | SI | QuestionAnswerLink |
| CON_ReasonDeprecated | varchar |  |  | SI | Deprecated Reason |
| CON_RowId | varchar |  |  | NO | - |
| CON_Score | varchar |  |  | SI | Score |
| CON_Sequence | double |  |  | SI | Sequence |
| CON_SignificantLevel | varchar |  |  | SI | SignificantLevel |
| CON_SingleOption | varchar |  |  | SI | SingleOption |
| CON_TBLControl_DR | varchar |  | FK | SI | Des Ref SSUserDefWindowControl of ChildTable CONCo... |
| CON_Text | varchar |  |  | SI | Text |
| CON_UserDefControl_DR | bigint |  | FK | SI | Des Ref UserDefControl |
| CON_Values | varchar |  |  | SI | Values |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*