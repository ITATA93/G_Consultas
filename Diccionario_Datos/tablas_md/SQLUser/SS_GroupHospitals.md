# SQLUser.SS_GroupHospitals

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| HOSP_Childsub | double |  |  | NO | Childsub |
| HOSP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| HOSP_RBSequence | double |  |  | SI | RBSequence |
| HOSP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*