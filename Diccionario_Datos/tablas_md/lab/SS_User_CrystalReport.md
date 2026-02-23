# lab.SS_User_CrystalReport

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUCR_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SUCR_Childsub | double |  |  | NO | Childsub |
| SUCR_CrystalReport | varchar |  |  | SI | Crystal Report |
| SUCR_Report_DR | varchar |  | FK | SI | Des Ref Report |
| SUCR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*