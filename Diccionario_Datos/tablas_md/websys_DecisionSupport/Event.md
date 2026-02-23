# websys_DecisionSupport.Event

**Schema:** websys_DecisionSupport
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
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
| IgnoreExternalTrigger | bit |  |  | SI | - |
| LastGenDate | varchar |  |  | SI | - |
| LastGenTime | varchar |  |  | SI | - |
| LastGenUser | bigint |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| RecordedEventUser | bigint |  |  | SI | - |
| RestrictionBlanksFail | varchar |  |  | SI | - |
| RestrictionExist | bit |  |  | SI | - |
| RestrictionGroupList | varchar |  |  | SI | - |
| RestrictionHospitalList | varchar |  |  | SI | - |
| RestrictionLocationList | varchar |  |  | SI | - |
| RestrictionLocationTypeList | varchar |  |  | SI | - |
| RestrictionUserList | varchar |  |  | SI | - |
| RestrictionWorkFlowList | varchar |  |  | SI | - |
| RuleCategory | bigint |  |  | SI | - |
| UpdateDate | varchar |  |  | SI | - |
| UpdateTime | varchar |  |  | SI | - |
| UpdateUser | bigint |  |  | SI | - |
| UseInDPL | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*