# lab.CT_Container

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCON_RowID | varchar | PK |  | NO | - |
| CTCON_Code | varchar |  |  | NO | Code |
| CTCON_Comment | varchar |  |  | SI | Comment |
| CTCON_Description | varchar |  |  | SI | Description |
| CTCON_Label_DR | varchar |  | FK | SI | Label DR |
| CTCON_Manufacturer_DR | varchar |  | FK | SI | Manufacturer |
| CTCON_Max_Volume | double |  |  | SI | Max Volume |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*