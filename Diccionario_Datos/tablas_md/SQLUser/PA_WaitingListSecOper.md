# SQLUser.PA_WaitingListSecOper

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SECOP_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| SECOP_Childsub | double |  |  | NO | Childsub |
| SECOP_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| SECOP_Operation_DR | bigint |  | FK | SI | Des Ref ORCOperation |
| SECOP_Package_DR | varchar |  | FK | SI | Des Ref PAPersonPackage |
| SECOP_RowId | varchar |  |  | NO | - |
| SECOP_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| SECOP_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| SECOP_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*