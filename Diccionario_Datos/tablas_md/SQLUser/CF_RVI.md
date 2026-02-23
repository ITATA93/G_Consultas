# SQLUser.CF_RVI

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RVI_RowId1 | double | PK |  | NO | - |
| ChildQ15DR | - |  |  | SI | Child Reference: Procedimientos Secundarios |
| Q13Q1 | - |  |  | SI | Hora |
| Q13Q2 | - |  |  | SI | Medicamento |
| Q13Q3 | - |  |  | SI | Dosis |
| Q13Q4 | - |  |  | SI | Vía de Administración |
| Q13Q5 | - |  |  | SI | Responsable |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RVI_PreviousClaim | varchar |  |  | SI | Previous Claim |
| RVI_RowId | double |  |  | NO | CF_RVI Row ID |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*