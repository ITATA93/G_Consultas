# web_Msg_DecisionSupport.Event

**Schema:** web_Msg_DecisionSupport
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AuthorUser | bigint |  |  | SI | - |
| AuthorityFreeText | varchar |  |  | SI | - |
| AuthorityUser | bigint |  |  | SI | - |
| Code | varchar |  |  | SI | - |
| ConditionGrouping | varchar |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| EnhancedMonitor | varchar |  |  | SI | - |
| EvaluateAgainstEpisode | bit |  |  | SI | - |
| EvaluateAgainstLabEpisode | bit |  |  | SI | - |
| EventCubeList | varchar |  |  | SI | - |
| EventError | varchar |  |  | SI | - |
| EventStatus | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IgnoreExternalTrigger | bit |  |  | SI | - |
| LastGenDate | varchar |  |  | SI | - |
| LastGenTime | varchar |  |  | SI | - |
| LastGenUser | bigint |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReadOnly | bit |  |  | SI | - |
| RecordedEventUser | bigint |  |  | SI | - |
| RestrictionBlanksFail | varchar |  |  | SI | - |
| RestrictionExist | bit |  |  | SI | - |
| RestrictionGroupList | varchar |  |  | SI | - |
| RestrictionHospitalList | varchar |  |  | SI | - |
| RestrictionLocationList | varchar |  |  | SI | - |
| RestrictionLocationTypeList | varchar |  |  | SI | - |
| RestrictionUserList | varchar |  |  | SI | - |
| RestrictionWorkFlowList | varchar |  |  | SI | - |
| RowID | varchar |  |  | SI | - |
| RuleCategory | bigint |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| UpdateDate | varchar |  |  | SI | - |
| UpdateTime | varchar |  |  | SI | - |
| UpdateUser | bigint |  |  | SI | - |
| UseInDPL | bit |  |  | SI | - |
| WizardMode | bit |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*