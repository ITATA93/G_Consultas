# lab.SS_User_HospitalAccess

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUHOS_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SUHOS_Hospital_DR | varchar |  | FK | NO | Des Ref Hospital |
| SUHOS_PreviousResults | varchar |  |  | SI | Previous Results |
| SUHOS_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*