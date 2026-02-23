# SQLUser.PA_WaitingListSecondaryProc

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SP_ParRef | bigint | PK |  | NO | - |
| SP_BodySite_DR | bigint |  | FK | SI | - |
| SP_Childsub | double |  |  | NO | Childsub |
| SP_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| SP_Operation_DR | bigint |  | FK | SI | PA_WaitingList Parent Reference |
| SP_Procedure_DR | bigint |  | FK | SI | - |
| SP_Qualifier_DR | varchar |  | FK | SI | - |
| SP_RowId | varchar |  |  | NO | - |
| SP_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| SP_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*