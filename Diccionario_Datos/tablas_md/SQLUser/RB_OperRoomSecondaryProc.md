# SQLUser.RB_OperRoomSecondaryProc

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SECPR_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| SECPR_BodySite_DR | bigint |  | FK | SI | Des Ref OECBodySite |
| SECPR_Childsub | double |  |  | NO | Childsub |
| SECPR_DateOper | date |  |  | SI | Date of Operation |
| SECPR_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| SECPR_Operation_DR | bigint |  | FK | SI | Des Ref ORCOperation |
| SECPR_Procedure_DR | bigint |  | FK | SI | Des Ref PACStatePPP |
| SECPR_Qualifier_DR | varchar |  | FK | SI | Des Ref ORCProcedureQualifier |
| SECPR_RowId | varchar |  |  | NO | - |
| SECPR_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| SECPR_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |
| SECPR_TimeOper | time |  |  | SI | Time of Operation |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*