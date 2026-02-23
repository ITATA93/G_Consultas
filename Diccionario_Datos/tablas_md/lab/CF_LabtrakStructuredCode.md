# lab.CF_LabtrakStructuredCode

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFLSC_ParRef | bigint | PK |  | NO | CF_LabTrak Parent Reference |
| CFLSC_DefaultEntryType | varchar |  |  | SI | Default Entry Type |
| CFLSC_Description | varchar |  |  | SI | Interface Description |
| CFLSC_Length | double |  |  | SI | Length |
| CFLSC_QuickEntry | varchar |  |  | SI | Quick Entry |
| CFLSC_RowID | varchar |  |  | NO | - |
| CFLSC_Sequence | double |  |  | NO | Sequence |
| CFLSC_Type | varchar |  |  | NO | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*